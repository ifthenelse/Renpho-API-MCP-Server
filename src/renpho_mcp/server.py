"""Read-only MCP server over the renpho-api SDK. Output is compact TSV to save tokens."""

import os
import time
from datetime import date, datetime, timedelta, timezone

from mcp.server.mcpserver import MCPServer
from renpho import RenphoClient
from renpho.constants import GIRTH_SITES, METRICS
from renpho.girth import normalize_girth

TTL = 900  # seconds a fetched history stays cached
UNITS = {k: u for k, _, u in METRICS}
SCALE_FIELDS = list(UNITS)
GIRTH_FIELDS = [s for _, s, _ in GIRTH_SITES] + ["whr"]
DEFAULT_SCALE = "weight,bodyfat,muscle"

mcp = MCPServer("renpho", instructions="Renpho body data. Pick few metrics, narrow dates, use period to shrink output.")
_client: RenphoClient | None = None
_cache: dict[str, tuple[float, list]] = {}


def _cached(key: str, fetch):
    hit = _cache.get(key)
    if hit and time.monotonic() - hit[0] < TTL:
        return hit[1]
    rows = fetch()
    _cache[key] = (time.monotonic(), rows)
    return rows


def _login() -> RenphoClient:
    global _client
    if _client is None:
        _client = RenphoClient(os.environ["RENPHO_EMAIL"], os.environ["RENPHO_PASSWORD"])
        _client.login()
    return _client


def _scale_rows() -> list[tuple[str, dict]]:
    """(local 'YYYY-MM-DD HH:MM', {metric: float}) newest first; 0/None = not measured."""

    def fetch():
        out = []
        for m in _login().get_all_measurements():
            ts = m.get("timeStamp") or 0
            ts = ts / 1000 if ts > 1e12 else ts
            when = str(m.get("localCreatedAt") or "")[:16] or datetime.fromtimestamp(ts, timezone.utc).strftime(
                "%Y-%m-%d %H:%M"
            )
            vals = {k: float(m[k]) for k in SCALE_FIELDS if isinstance(m.get(k), int | float) and m[k]}
            out.append((when, vals))
        return out

    return _cached("scale", fetch)


def _girth_rows() -> list[tuple[str, dict]]:
    def fetch():
        out = []
        for g in _login().get_girth_measurements():
            n = normalize_girth(g)
            if d := n.pop("date", None):
                out.append((d, n))
        return out

    return _cached("girth", fetch)


def _bucket(when: str, period: str) -> str:
    if period == "month":
        return when[:7]
    if period == "week":
        d = date.fromisoformat(when[:10])
        return (d - timedelta(days=d.weekday())).isoformat()
    return when[:10] if period == "day" else when


def _fmt(v: float | None) -> str:
    return (
        "" if v is None else f"{v:.1f}".rstrip("0").rstrip(".") if abs(v) >= 10 else f"{v:.2f}".rstrip("0").rstrip(".")
    )


def _table(rows, fields: list[str], valid: list[str], since: str, until: str, period: str, limit: int) -> str:
    bad = [f for f in fields if f not in valid]
    if bad:
        return f"unknown: {','.join(bad)}. valid: {','.join(valid)}"
    if period not in ("", "day", "week", "month"):
        return "period must be day|week|month or empty"
    groups: dict[str, dict[str, list[float]]] = {}
    for when, vals in rows:  # rows are newest first; dict keeps that order
        if (since and when[:10] < since) or (until and when[:10] > until):
            continue
        g = groups.setdefault(_bucket(when, period), {})
        for f in fields:
            if f in vals:
                g.setdefault(f, []).append(vals[f])
    lines = ["date\t" + "\t".join(fields)]
    for key, g in list(groups.items())[: max(limit, 1)]:
        cells = [_fmt(sum(g[f]) / len(g[f])) if f in g else "" for f in fields]
        lines.append(key + "\t" + "\t".join(cells))
    if len(groups) > limit:
        lines.append(f"# {len(groups) - limit} older rows omitted (raise limit or narrow since/until)")
    return "\n".join(lines) if len(lines) > 1 else "no data"


def _split(s: str) -> list[str]:
    return [x.strip() for x in s.split(",") if x.strip()]


@mcp.tool(structured_output=False)
def summary() -> str:
    """Latest scale reading, 30-day change per metric, record count and date range. Start here."""
    rows = _scale_rows()
    if not rows:
        return "no scale data"
    latest_when = rows[0][0]
    cutoff = (date.fromisoformat(latest_when[:10]) - timedelta(days=30)).isoformat()
    lines = [f"{len(rows)} records {rows[-1][0][:10]}..{latest_when[:10]}; latest {latest_when}"]
    for k, v in rows[0][1].items():
        old = next((r[1][k] for r in reversed(rows) if r[0][:10] >= cutoff and k in r[1]), v)
        lines.append(f"{k}\t{_fmt(v)}{UNITS[k]}\t30d {'+' if v >= old else ''}{_fmt(v - old)}")
    girth = _girth_rows()
    if girth:
        lines.append(f"girth: {len(girth)} records, latest {girth[0][0]}")
    return "\n".join(lines)


@mcp.tool(structured_output=False)
def measurements(
    metrics: str = DEFAULT_SCALE, since: str = "", until: str = "", period: str = "", limit: int = 30
) -> str:
    """Scale history as TSV, newest first. metrics: comma list of weight,bmi,bodyfat,water,muscle,bone,bmr,visfat,subfat,protein,bodyage,sinew,fatFreeWeight,heartRate (kg, % of body, bmr kcal). since/until: YYYY-MM-DD. period: day|week|month averages rows (cheapest for trends)."""
    return _table(_scale_rows(), _split(metrics), SCALE_FIELDS, since, until, period, limit)


@mcp.tool(structured_output=False)
def girth(sites: str = "waist,hip,whr", since: str = "", until: str = "", period: str = "", limit: int = 30) -> str:
    """Tape-measure history as TSV (cm), newest first. sites: comma list of neck,shoulder,chest,waist,hip,abdomen,arm,left_arm,right_arm,thigh,left_thigh,right_thigh,calf,left_calf,right_calf,whr. Same filters as measurements."""
    return _table(_girth_rows(), _split(sites), GIRTH_FIELDS, since, until, period, limit)


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
