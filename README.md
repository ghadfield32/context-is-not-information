# Context Is Not Information

**Testing Daily and Transition Signals in NBA Player Forecasting**
Geoffrey Hadfield · World Model Sports LLC · geoff@worldmodelsports.com

## ⚠️ Read this first: this package is NOT yet independently reproducible

`REPRODUCTION_BLOCKER.md` documents a hard blocker. The transition experiment's
original inputs no longer exist, and the recorded bytes differ from the ones the
study used:

| Input | Original SHA-256 | Current bytes |
|---|---|---|
| `player_game_fact.parquet` | `368dbee5…` | `a9364e6f…` |
| `team_game_fact.parquet` | `48b16b97…` | `199ad56c…` |

The runner refuses on hash mismatch, and no per-row prediction tables are
committed. A genuine evaluation dataset therefore **cannot be constructed** from
what is available. Do not treat this repository as a reproducible artifact yet.

## The question

Player-value systems routinely add rest, venue, team and transition context to
player-history features, on the assumption that more context means a better
forecast. This study tests that assumption directly in two retrospective NBA
tasks.

## The finding

**Context is not automatically information.** It can help slightly, or it can
hurt substantially, depending on the prediction regime.

| Task | Sample | Result |
|---|---|---|
| Daily production | 68,546 appearances | Context **helps** slightly: MAE 5.1311 → 5.1158 (**0.30%**) |
| Consecutive-day cohort | 10,259 records | Context **hurts**: MAE 5.3137 → 5.3312 |
| Post-trade conditional minutes | 313 episodes | Richer destination context **hurts badly**: MSE 41.56 → 49.89 |

The transition failure is not marginal. The context-minus-history difference is
**+8.33** with a player-cluster interval of **[3.12, 14.21]**, and context loses
on more episodes than it wins (**148 vs 165**). **96.45%** of the net excess
squared error sits in the earliest issuance fold, which trains the larger model
on only 58 episodes.

A sensitivity clustered by issuance date instead gives **[−0.07, 20.78]** — so
the *dependence choice itself matters*, which is part of the finding rather than
a footnote.

## Why it matters

Both tasks were run with past-only, cohort-aware evaluation on identical
episodes. The lesson is procedural: context features should have to **earn**
inclusion through evaluation under the correct target, timing, cohort and sample
size — not be added because they are available.

This sits alongside two companion results from the same program:

- **PMI** — *a rating is not a forecast*
- **E1** — *more measured state is not automatically more information*
- **DPV** — *context is not automatically information*

## What this study does NOT claim

Not causal rest effects. Not participation forecasts. Not injury modeling. Not
trade profitability, financial benefit, or optimal trade timing. Not
coach/team context improving forecasts. Not validation of a deployed system.
Those remain separate, unexecuted studies.

## Files

| File | Purpose |
|---|---|
| `abstract.txt` / `abstract.md` | The abstract |
| `CLAIM_LEDGER.md` | Every claim → evidence → limitation |
| `DATA.md` | Data provenance and the reproduction boundary |
| `RIGHTS.md` | Rights position; no licence asserted |
| `REPRODUCTION_BLOCKER.md` | Why the repo is not yet reproducible |
