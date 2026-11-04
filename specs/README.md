# Specs

Every story gets one folder, named after its Jira key: `specs/<JIRA-KEY>/`.

| File | Written by | Purpose |
| --- | --- | --- |
| `<slug>.feature` | Spec and dev agent, copied word for word from the approved Gherkin in Jira | Source of truth for behaviour; tests bind to it |
| `spec.md` | Spec and dev agent, from `specs/_template/spec.md` | How the behaviour is built: files, API, UI, assumptions |

Rules:

- The `.feature` file must match the Gherkin approved at G2 (Definition of Ready). Changing it means changing the story first.
- Tests are generated from the `.feature` file, never from the code.
- `BASE-1/` is the baseline example to copy.
