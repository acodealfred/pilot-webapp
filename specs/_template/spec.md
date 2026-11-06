# <JIRA-KEY>: <Story title>

**Story:** <link to Jira ticket> · **Status:** Draft | Implemented

## Behaviour

What the user can do after this change, in two or three sentences. Copy nothing from the story that the `.feature` file already says.

## Design

- Files to add or change, and why.
- API changes: method, path, request and response bodies.
- UI changes: page, elements and their `data-testid` values.

## Out of scope

- What this change deliberately does not do.

## Assumptions

- Anything decided without the story stating it. Each one must be confirmed at code review (G4).

## Tests

| Scenario (from the `.feature` file) | Test |
| --- | --- |
| <scenario name> | `tests/bdd/test_<key>_<slug>.py` or `tests/e2e/test_<key>_<slug>.py` |
