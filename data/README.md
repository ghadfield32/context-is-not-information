# Data package status

No raw NBA-derived data or per-row historical evaluation table is currently
bundled in this repository.

See:

- `../DATA.md`;
- `../RIGHTS.md`;
- `../REPRODUCTION_BLOCKER.md`.

## Intended future public evidence tables

When rights and source-vintage requirements are satisfied, the minimal public
research package should contain tables sufficient to reproduce the paper's
statistics without exposing unrelated warehouse data.

### Daily task

Suggested fields:

- anonymous player id;
- season;
- evaluation date;
- calendar-block id;
- actual production proxy;
- history prediction;
- context prediction;
- consecutive-day indicator.

### Transition task

Suggested fields:

- anonymous episode id;
- anonymous player id;
- evaluation fold;
- player cluster id;
- issuance-date cluster id;
- target conditional minutes;
- recent-minutes prediction;
- prior-season prediction;
- history-ridge prediction;
- context-ridge prediction.

Any future export must undergo a separate data-rights and disclosure review.
Anonymization alone does not establish redistribution rights.
