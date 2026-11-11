# PIL-1: Show the app version on an About page

**Story:** PIL-1 (Jira) · **Status:** Implemented

## Behaviour

`GET /api/version` returns the app version. The `/about` page reads it and displays it. Other paths do not show a version.

## Design

- `backend/app/main.py`: `APP_VERSION = "0.1.0"` constant (single backend source) and `GET /api/version` returning `{"version": APP_VERSION}`.
- `frontend/src/main.ts`: route on `location.pathname`; `/about` renders an About page with the version in `data-testid="app-version"`. Other paths render the home page as before. If the endpoint fails, the page shows no version element.
- Served by the existing SPA fallback; no new dependency.

## Out of scope

- Build number, commit hash, release date, environment name.
- Navigation links to the About page.
- Changing how the version is released or bumped.

## Assumptions

- Version is `0.1.0`, matching `frontend/package.json`; the backend holds its own constant, so both must be bumped together (authoritative source is open for the Product Owner).
- `/about` needs no login and shows only the version.
- The feature file is split across two test modules: scenario 1 in BDD (no browser), scenarios 2 and 3 in a browser test (`_ui.py`, marked e2e) with their page steps.

## Tests

| Scenario (from the `.feature` file) | Test |
| --- | --- |
| Version endpoint reports the app version | `tests/bdd/test_pil_1_about_version.py` |
| About page displays the app version | `tests/e2e/test_pil_1_about_version_ui.py` |
| Unknown page does not show a version | `tests/e2e/test_pil_1_about_version_ui.py` |
