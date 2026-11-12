# Runbooks

Operational procedures: deployment, validation, alert response, recovery, common failure modes.
Each runbook states owner, prerequisites, steps, verification and rollback.

## Common failure modes (owner: Andrea Collet)
| Symptom | Likely cause | Fix |
| --- | --- | --- |
| Tool error `KeyError: 'RENPHO_EMAIL'` | `.env` missing or not passed | use `--env-file` with an absolute path |
| `Login failed: code=..., msg=...` | wrong credentials, or Renpho rejected the login | check the account in the Renpho app; rotate password if exposed |
| `no data` | filters exclude everything, or the account has no records for that device | widen `since`/`until`; try `summary` |
| Stale numbers after a new weigh-in | 15-minute in-memory cache | wait, or restart the container (each client session starts a fresh one) |
| Everything errors after it worked | Renpho changed its API | check for a newer `renpho-api`, bump it (needs review), rebuild |
| Client shows no tools | `-i` missing from `docker run`, or image not built | stdio needs `-i`; rerun the smoke test |
