from renpho_mcp import server

ROWS = [
    ("2024-03-10 08:00", {"weight": 80.0, "bodyfat": 20.0}),
    ("2024-03-09 08:00", {"weight": 81.0}),
    ("2024-02-01 08:00", {"weight": 82.0, "bodyfat": 22.0}),
]


def table(**kw):
    a = {
        "fields": ["weight", "bodyfat"],
        "valid": server.SCALE_FIELDS,
        "since": "",
        "until": "",
        "period": "",
        "limit": 30,
    }
    return server._table(ROWS, **{**a, **kw})


def test_raw_rows_blank_missing():
    assert table().splitlines()[2] == "2024-03-09 08:00\t81\t"


def test_month_average_and_filter():
    out = table(period="month", since="2024-03-01").splitlines()
    assert out == ["date\tweight\tbodyfat", "2024-03\t80.5\t20"]


def test_week_bucket_is_monday():
    assert table(period="week", until="2024-03-31").splitlines()[1].startswith("2024-03-04")


def test_limit_and_unknown_metric():
    assert "older rows omitted" in table(limit=1)
    assert table(fields=["nope"]).startswith("unknown: nope")


def test_summary_delta(monkeypatch):
    monkeypatch.setattr(server, "_scale_rows", lambda: ROWS)
    monkeypatch.setattr(server, "_girth_rows", list)
    out = server.summary()
    assert "weight\t80kg\t30d -1" in out  # vs 2024-03-09 (oldest within 30d)
