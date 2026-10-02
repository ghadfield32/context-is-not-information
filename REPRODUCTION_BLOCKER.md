# DPV — reproduction blocker (read this first)

**This repository is not reproducible from its own contents, and cannot be made so
tonight. Do not submit it as an open-reproducibility artifact until the inputs
below are recovered.**

## What is blocked

The transition experiment's original inputs **no longer exist in the working
tree**, and the recorded bytes differ from the ones the study used.

| Input | Original expected SHA-256 (used by the study) | Current bytes on disk |
|---|---|---|
| `player_game_fact.parquet` | `368dbee5fb6aaf027d9268521e64c34c45cd50a7dd77c4579b2dedf965da032e` | `a9364e6f01c03854b125e35177d017e4906c11de6b01c9f0257634368512488d` |
| `team_game_fact.parquet` | `48b16b979f01121ca2c5dd0bdb1afb1ea13b89036b1da63cb0a77c273e52bd03` | `199ad56ce16a08a95b2449f599204d8292f4b41dda668bb72ec99a940fe91904` |
| `transaction_events.parquet` | `bafd95455af3fc4600461c4941a17dc6ebe82a2967422559c42ac8966dd32744` | unchanged (present) |

The source documentation states plainly that the original runner **refuses**
(`Source hash mismatch: player_game_fact.parquet`) before writing any output, and
that no expected hash was overwritten. A read-only search of 71 retained large
player/team-game candidate files found **no exact copy**; that is a bounded
search, not proof that no copy exists elsewhere.

## Exhaustive recovery attempt (2026-10-01)

A recovery sweep was run at the submission deadline. It enumerated every
`player_game_fact.parquet` and `team_game_fact.parquet` plus every
`*fact*.parquet` on the local volumes and hashed all of them:

```
files hashed : 2183
MATCHES      : 0
```

Neither original file is present anywhere on `C:` or `D:`. Combined with the
source's own bounded search, the "best route" — recover the exact bytes and re-run
the experiment — is **closed**.

It remains possible that a copy exists on an offline archive or NAS not mounted
here. Nothing in this repository asserts that the bytes are gone forever; it
asserts only that they are not available to reproduce from.

A *different* vintage exists and is separately declared (manifest
`c3cd56a9ff983ff6ce380bc1a3c6445b46effd072ac216636489e7a78978f4e2`, explicitly
stated to be different bytes). Refitting from that vintage would produce
**different numbers** than the ones the abstract reports.

## What this means

Neither available route yields a truthful reproduction:

- **Refit from current bytes** → different vintage → does not reproduce the abstract.
- **Transcribe the aggregate tables into a CSV** → not a reproduction; it is a copy
  of the reported numbers, which proves only internal consistency, not that the
  pipeline produces them.

No per-row prediction tables (episode ids, targets, per-model predictions) are
committed. Only aggregate reports exist. Therefore a genuine evaluation dataset
**cannot be constructed** from what is available.

## What is needed to unblock

1. The original `player_game_fact.parquet` and `team_game_fact.parquet` bytes, or
   a verified copy of them, matching the original hashes above.
2. Re-run `entrant_minutes_run.py` against those exact bytes to regenerate the
   episode-level predictions.
3. Export a privacy-reviewed episode table (anonymous ids, target, and the four
   model predictions) sufficient to recompute MSE, the paired differences, both
   cluster intervals, the 148/165 direction count, and the fold-1 share.
4. Repeat for the daily task from a pinned box-score vintage.
5. Regenerate this receipt from a clean clone, then a non-author review.

Until (1) is satisfied, the transition half of the paper is a **documented
historical result**, not a reproducible artifact — exactly the L2/L3 distinction
used elsewhere in this program, and the same distinction the source documents
already draw.
