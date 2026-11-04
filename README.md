# Spear818 pilot web app

A deliberately small web app used to test the Spear818 agentic SDLC pipeline: Claude agents draft stories, build them and test them, and people approve each step.

- **Backend:** FastAPI (Python 3.13), JSON API under `/api`
- **Front end:** TypeScript and Vite, served by the backend
- **Tests:** `pytest`, `pytest-bdd` (from `specs/` feature files) and Playwright

## Run it

With Docker (no local Python or Node setup needed):

```bash
docker compose up --build
# open http://localhost:8000
```

For development and tests, see `CLAUDE.md`.

## How changes arrive

Every change is a pull request linked to a Jira ticket in the `PIL` project, with its spec in `specs/<JIRA-KEY>/`. CI must pass and a person must approve before merging.
