# Development baseline and data-vintage status

Recorded 2026-10-02. This file is development metadata; it is not a result and
does not alter any claim boundary.

## Frozen baseline

| Item | Value |
|---|---|
| Development branch head | `5e9a2d028906c080509e6fbd0a4d96a764264219` |
| Submitted snapshot / `main` | `d867cc5e26c7aee1ac71c7c189c6186323a40cd3` (immutable) |
| Integrity invariant | fresh clone → `verify_integrity.py` → ALL PASS |

`main` and `submitted-abstract-2026-10-01` must not be modified. This development
head is the source point for all new work. `abstract.md` and `abstract.txt` are
byte-identical across the snapshot and this branch.

## Three scientific generations, never mixed

| Lane | Purpose | Status |
|---|---|---|
| DPV historical V1 | the submitted findings | frozen; development-exposed |
| `DPV-TRAJECTORY-RETRO-NV1` | new-vintage H0→H1→H2 ladder | **premise not yet satisfied — see below** |
| Registered C0/C1/C2 | prospective career/opportunity confirmation | registered 2026-10-01, zero fits, unchanged |

The new ladder is intended to run **alongside** the frozen combined H1T design,
not to supersede it. Prior workload-trajectory work already exists and did not
improve on the frozen comparator on 124 development-exposed episodes
(MSE 25.42 versus 23.18; interval crossing zero). That is why the ladder is
separately versioned rather than refit onto the H1T lane.

## Data-vintage status — verified 2026-10-02

Pinned bytes currently available locally, with sha256 computed over the files as
they exist now:

| Input | sha256 | Rows | Date range |
|---|---|---:|---|
| `player_game_fact.parquet` | `bcf7207d3c820c974c1bf5ab7f74039266e0ff69b385b86720da80d50d642743` | 283,210 | 2015-10-27 → 2026-06-13 |
| `team_game_fact.parquet` | `1b887bf6083738bebc2967f156160b419b8c372a4ef6362ba9b2540490a91c82` | 26,600 | 2015-10-27 → 2026-06-13 |
| `transaction_events.parquet` | `2cbd79c24ce277e34d0d6b3cd4ab71b431cbdeb74aeab63e73dd13d02139cae2` | 9,926 | 2015-07-01 → 2026-10-01 |

### Finding: these bytes are not a new-outcome vintage

The game facts end at **2026-06-13** and contain **zero 2026-27 games**
(`SEASON_ID` runs 2015-16 → 2025-26). The only inputs newer than the V1 study are
**459 transaction events dated after 2026-06-13**, and those have **no matured
destination outcomes** to score: the estimand's censored 30-day window requires
post-transaction appearances that do not exist until 2026-27 games are played.

Consequence: re-pinning these files under a new sha256 produces a *reproducible,
hash-pinned pipeline over the same evaluation games as V1*. That is a
reproducibility contribution, not new evidence. Presenting it as a "new vintage"
would be a label change rather than new information.

### What would actually satisfy the new-vintage premise

1. **New outcome seasons.** Accumulate 2026-27 games so post-June transactions
   have mature, scoreable destinations. This is time-gated, not an engineering
   task.
2. **Explicit re-characterization.** If the archived years are reused, describe
   the study as a *hash-pinned reproducible re-evaluation on the archived years*
   and drop any implication of untouched validation. This is legitimate and
   useful, but it is a different claim.

The registered prospective C0/C1/C2 lane is the correct home for genuinely new
cases, once its source roles carry real `available_at <= issuance` evidence and
2026-27 outcomes mature.

## H0 feature family (confirmed against source)

`scripts/nba_value/research/entrant_minutes.py` defines the history family as:

```
HISTORY_FEATURES = ['recent_minutes', 'prior_minutes', 'recent_count', 'recent_gap_days']
```

with `Ridge(alpha=1.)` and train-only `StandardScaler`, and cohorts
`recent_band` (<10 / 10-<20 / 20-<30 / 30+) and `gap_band` (<=7 / 8-30 / >30).
Any H0 contract should freeze exactly this family before fitting.

## Reproduction boundary (unchanged)

The V1 historical inputs `player_game_fact` `368dbee5…` and `team_game_fact`
`48b16b97…` remain absent at their recorded hashes, and no per-row prediction
table was retained. See `REPRODUCTION_BLOCKER.md`.
