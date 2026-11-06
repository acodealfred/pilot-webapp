# BASE-1: Service health

**Story:** Baseline (no Jira ticket) · **Status:** Implemented

## Behaviour

`GET /api/health` returns HTTP 200 with the body `{"status": "ok"}`. The home page shows this status.

## Design

- Endpoint in `backend/app/main.py`.
- Home page calls the endpoint and shows the value in the element with `data-testid="health-status"`.

## Tests

| Scenario | Test |
| --- | --- |
| Health endpoint reports ok | `tests/bdd/test_base_1_health.py` |
| Home page shows status | `tests/e2e/test_home.py` |
