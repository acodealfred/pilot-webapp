# PIL-4: Search feature requests by text

**Story:** Jira PIL-4 · **Status:** Implemented

## Behaviour

On `/feature-requests` a search box filters the list as the user types. Only requests whose title contains the text are shown, still newest first. When nothing matches, the message "No requests found" is shown.

## Design

- `backend/app/main.py`: `GET /api/feature-requests` takes an optional query parameter `q`. The trimmed, case-insensitive text is matched against the title as a substring. Missing or blank `q` returns everything.
- `frontend/src/main.ts`: search input above the list; each input event reloads the list with `?q=`. Out-of-order responses are ignored.
  - `data-testid`: `request-search` (search box), `request-empty` (message, shown only when a search is active and nothing matches). `request-list` and `request-item` are reused.
- `tests/bdd/conftest.py`: new reusable step "the response is an empty list".
- No new dependencies.

## Out of scope

- Searching anything other than feature requests.
- Category filter, sorting, paging, highlighting, search history, keeping the search text across reloads.

## Assumptions

- "Existing features" means the feature request list, the only list in the app.
- Search matches the title only (not description or category), ignoring case, on any part of the title.
- The list updates while typing; there is no search button.
- Leading and trailing spaces are ignored; an empty search shows all requests.
- Matches keep newest-first order.
- The empty message is "No requests found" and is not shown when the list is empty without a search.
- Scenario 4 assumes no stored request contains "zzz".

## Tests

| Scenario (from the `.feature` file) | Test |
| --- | --- |
| Search shows only matching requests | `tests/e2e/test_pil_4_search_feature_requests_ui.py` |
| Search with no match shows a message | `tests/e2e/test_pil_4_search_feature_requests_ui.py` |
| Clearing the search shows all requests again | `tests/e2e/test_pil_4_search_feature_requests_ui.py` |
| API filters requests by search text | `tests/bdd/test_pil_4_search_feature_requests.py` |

`tests/api/test_feature_requests.py` adds unit tests for case-insensitive, partial, trimmed and ordered matching.
