# Pilot web app: rules for agents

This repo is the pilot app for the Spear818 agentic SDLC. Agents work here through pull requests only. A person reviews and merges every PR (gate G4).

## Stack and layout

| Area | Location | Notes |
| --- | --- | --- |
| Backend | `backend/app/` | FastAPI, Python 3.13. API routes live under `/api` |
| Front end | `frontend/src/` | TypeScript and Vite, no framework. Built into `frontend/dist`, which the backend serves |
| Specs | `specs/<JIRA-KEY>/` | `spec.md` and the story's `.feature` file. See `specs/README.md` |
| API and BDD tests | `tests/api/`, `tests/bdd/` | `pytest`, `pytest-bdd`. Reusable API steps are in `tests/bdd/conftest.py` |
| Browser tests | `tests/e2e/` | Playwright (Python), marked `@pytest.mark.e2e` |

## Commands

```bash
pip install -r backend/requirements-dev.txt
(cd frontend && npm install && npm run build)
ruff check backend tests
pytest                                    # unit and BDD tests
uvicorn app.main:app --app-dir backend --port 8000 &
pytest -m e2e --base-url http://localhost:8000
```

## Working on a story

1. Branch: `<JIRA-KEY>-<short-slug>`, for example `PIL-1-about-page`.
2. Copy the approved Gherkin from the Jira ticket into `specs/<JIRA-KEY>/<slug>.feature`, word for word.
3. Write `specs/<JIRA-KEY>/spec.md` from `specs/_template/spec.md`.
4. Write tests that bind to the `.feature` file (`scenarios("<JIRA-KEY>/<slug>.feature")`), then the code.
5. Run lint and all tests. Every commit message starts with the Jira key: `PIL-1: Add About page`.
6. Open a PR titled `<JIRA-KEY>: <story title>` whose description links the ticket and lists any assumptions.

## Rules

- Never push to `main`, never merge, never force-push.
- Never edit a `.feature` file to make a test pass. If the story is wrong, stop and say so in the PR.
- Give every UI element a test uses a `data-testid`.
- Add a dependency only when the story needs it, and say why in `spec.md`.
- No secrets, tokens or real personal data in code, tests or fixtures.
- Keep the change to what the story asks for.
