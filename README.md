# Context Is Not Information

**Testing Daily and Transition Signals in NBA Player Forecasting**

Geoffrey Hadfield · World Model Sports LLC · geoff@worldmodelsports.com

## Start here

This repository has two distinct states:

- **Submitted abstract snapshot:** branch [`submitted-abstract-2026-10-01`](https://github.com/ghadfield32/context-is-not-information/tree/submitted-abstract-2026-10-01)
- **Full-paper development:** branch [`full-paper-development`](https://github.com/ghadfield32/context-is-not-information/tree/full-paper-development)

The submitted abstract is preserved and should not be rewritten retroactively.
The development branch is where additional diagnostics, manuscript material and
future experiments belong.

## Research question

NBA player-value systems routinely add rest, venue, team and transition context
to player-history features. This project asks:

> **When does additional context actually improve an NBA player forecast, and
> when does it make the forecast worse?**

## Primary submitted findings

| Task | Population | Result |
|---|---:|---:|
| Daily production | 68,546 appearances | Context improves MAE **5.1311 → 5.1158** (~0.30%) |
| Consecutive-day cohort | 10,259 appearances | Context worsens MAE **5.3137 → 5.3312** |
| Transition history ridge | 313 episodes | MSE **41.56** |
| Rich destination context | 313 episodes | MSE **49.89** |

Transition context-minus-history:

- MSE difference **+8.33**;
- player-cluster 95% interval **[3.12, 14.21]**;
- issuance-date sensitivity **[-0.07, 20.78]**;
- context improves 148 episodes and worsens 165;
- 96.45% of net excess squared error is concentrated in the earliest fold.

The core conclusion is:

> **Context is not automatically information.**

## Post-hoc diagnostics

Later diagnostics reduce the transition model's damage:

| Model | MSE | Status |
|---|---:|---|
| History-only ridge | 41.56 | Primary baseline |
| Rich destination context | 49.89 | Primary adverse result |
| Support-aware fallback | 43.94 | Post hoc diagnostic |
| Shrinkage | 41.43 | Post hoc diagnostic; reliable incremental gain not established |

These diagnostics do not retroactively change the submitted abstract.

## Full-paper navigation

- [`MANUSCRIPT.md`](MANUSCRIPT.md) — working full-paper draft
- [`RESULTS.md`](RESULTS.md) — compact numerical evidence
- [`SCIENTIFIC_STATUS.md`](SCIENTIFIC_STATUS.md) — what is primary, secondary, post hoc, planned or blocked
- [`CLAIM_LEDGER.md`](CLAIM_LEDGER.md) — submitted claim boundaries
- [`SYSTEM_STAGES.md`](SYSTEM_STAGES.md) — stage-by-stage system status
- [`RESEARCH_ROADMAP.md`](RESEARCH_ROADMAP.md) — H0/H1/H2, prospective C0/C1/C2, participation, rotations and decisions
- [`REPRODUCE.md`](REPRODUCE.md) — reproduction plan and closure criteria
- [`REPRODUCTION_BLOCKER.md`](REPRODUCTION_BLOCKER.md) — exact historical blocker
- [`DATA.md`](DATA.md) — data provenance
- [`RIGHTS.md`](RIGHTS.md) — third-party-data rights position
- [`data/README.md`](data/README.md) — intended future public evidence tables

## Current scientific boundary

This work supports:

1. a small average daily-context gain;
2. a clear short-rest failure cohort;
3. a strong player-history transition baseline;
4. material degradation from a richer destination-context specification;
5. evidence that support restrictions and shrinkage can reduce that damage;
6. the methodological requirement that context earn inclusion through
   temporally valid incremental evaluation.

This work does **not** yet establish:

- causal rest or injury effects;
- participation probability;
- coherent team rotations;
- optimal trade timing;
- trade profitability;
- financial benefit;
- prospective confirmation of the historical transition result.

## Reproduction status

The historical transition experiment is traceable to retained reports but is not
currently reproducible end to end from this standalone repository.

Two exact historical input files are no longer available at their recorded
hashes, and no episode-level target/prediction table was retained. The
hash-pinned runner correctly refuses to use a later vintage as though it were
the original experiment.

See [`REPRODUCE.md`](REPRODUCE.md) and
[`REPRODUCTION_BLOCKER.md`](REPRODUCTION_BLOCKER.md).

## Research direction

The next high-value development experiment is:

[
H0;(	ext{history})
ightarrow
H1;(	ext{workload trajectory})
ightarrow
H2;(	ext{production trajectory}).
]

A separate prospectively registered career/opportunity study remains distinct
and should not be rewritten based on historical H1/H2 results.

The longer-term dependency chain is:

[
Career ightarrow Opportunity ightarrow Participation ightarrow Workload
ightarrow Production ightarrow Rotation ightarrow TeamState ightarrow Decision.
]

Each layer must demonstrate incremental value for its own target and timing
before promotion.
