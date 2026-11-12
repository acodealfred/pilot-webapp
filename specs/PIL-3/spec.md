# PIL-3: Submit and view feature requests

**Story:** Jira PIL-3 · **Status:** Implemented

## Behaviour

A user opens `/feature-requests`, fills in a form (title, optional description, category) and sees the request appear at the top of the list on the same page. Invalid input shows an error next to the form.

## Design

- `backend/app/main.py`: in-memory list and two routes.
  - `POST /api/feature-requests` with body `title`, optional `description`, `category`. Returns 201 with the stored request. A blank or space-only title returns 422 with detail "Title is required". A category outside UI, Performance, Other returns 422 (schema validation).
  - `GET /api/feature-requests` returns the list, newest first.
- `frontend/src/main.ts`: new `/feature-requests` page with form and list.
  - `data-testid`: `request-title`, `request-description`, `request-category`, `request-submit`, `request-list`, `request-item`, `request-error`.
- No new dependencies.

## Out of scope

- Login, database or persistence, editing, deleting, voting, status, filtering, searching, paging.
- A navigation link to the page, length limits, and a cap on stored requests (open questions for the Product Owner).

## Assumptions

- A title of only spaces counts as empty; the title is stored trimmed.
- The description is optional and shown only when provided.
- Category is a fixed list; the form defaults to Other.
- Newest first is by submission order.
- The error text is "Title is required".
- The list is shared by all users of the running app and is empty at startup.
- The form clears after a successful submission.
- No length limits and no cap on the number of requests.
- The page is not linked from the home page.

## Tests

| Scenario (from the `.feature` file) | Test |
| --- | --- |
| Submitted request appears in the list | `tests/e2e/test_pil_3_feature_requests_ui.py` |
| Newest request is listed first | `tests/e2e/test_pil_3_feature_requests_ui.py` |
| Request without a title is rejected | `tests/e2e/test_pil_3_feature_requests_ui.py` |
| Request with an unknown category is rejected by the API | `tests/bdd/test_pil_3_feature_requests.py` |

`tests/api/test_feature_requests.py` adds unit tests for ordering, blank titles and the optional description.
