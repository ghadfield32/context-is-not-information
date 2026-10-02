# Data provenance and the reproduction boundary

## What the study used

Both tasks are retrospective evaluations over locally archived NBA box-score and
transaction records in the World Model Sports data environment.

| Task | Inputs | State |
|---|---|---|
| Daily production | Locally archived NBA box-score records; a versioned production proxy target | Aggregates committed; **no per-row table committed** |
| Transition | `player_game_fact.parquet`, `team_game_fact.parquet`, `transaction_events.parquet` | **Original bytes no longer present** (see `REPRODUCTION_BLOCKER.md`) |

The transaction capture supports **event-time reconstruction**, not authenticated
historical information availability. That distinction is load-bearing: the study
can order events historically; it cannot prove that every input was actually
available at issuance time in a live system.

## The production proxy

`PTS + 0.4*FG − 0.7*FGA − 0.4*(FTA−FT) + 0.7*REB + STL + 0.7*AST + 0.7*BLK − 0.4*TOV`

This is an explicitly versioned historical target and is **not** Hollinger Game
Score. Naming it accurately matters because the two are often conflated.

## Reproduction levels

| Level | State |
|---|---|
| L1 — reported-statistics replay | **Not available.** No per-row prediction tables are committed, so the reported statistics cannot be recomputed from this repository |
| L2 — reconstruction from retained inputs | **Blocked.** The original input bytes are gone and the runner refuses on hash mismatch |
| L3 — raw-source refit | **Not executable at the reported vintage.** Refitting from current bytes would use a different, separately declared vintage and produce different numbers |

There is no level at which this repository currently reproduces the abstract.

## Why not ship a transcription

Writing the aggregate tables into a CSV would let a reader re-derive the reported
numbers, but it would **not** be a reproduction: it would copy the outputs and
prove only that the arithmetic on them is self-consistent. That is exactly the
kind of artifact that looks reproducible and is not. It is refused here on
purpose, and the refusal is recorded rather than worked around.

## What a real reproduction requires

1. The original input bytes matching the recorded hashes.
2. A re-run of `entrant_minutes_run.py` on those bytes to regenerate episode-level
   predictions.
3. A privacy-reviewed episode export: anonymous episode and player ids, the
   issuance cluster, the target, and the four model predictions.
4. The same for the daily task from a pinned box-score vintage.
5. A clean-clone receipt, then an independent non-author review.

## Rights

See `RIGHTS.md`. Nothing here asserts a licence to redistribute NBA-derived data.
