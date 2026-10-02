# The stage-by-stage system

This is the operational breakdown behind the two experiments: what each stage
does, what was actually executed, and where each stage's evidence lives. It is
written so a reader can see **exactly which stages are established** and which
are not, without reading the full monorepo.

Status legend: **EXECUTED** (ran on real data) · **REPORTED** (result recorded) ·
**NOT EXECUTED** (no result) · **BLOCKED** (cannot be re-run as packaged).

---

## Stage 0 — Data acquisition and vintage pinning

| | |
|---|---|
| Purpose | Establish which bytes the study used, so results are attributable to a specific vintage |
| Method | Hash-pinned input manifests; the runner refuses on any hash mismatch before writing output |
| Status | **EXECUTED**, and it **FAILED CLOSED** — which is the reason this package is not reproducible |
| Evidence | `REPRODUCTION_BLOCKER.md`; source note stating `Source hash mismatch: player_game_fact.parquet` |

This stage did exactly what it was designed to do. It is a *feature* that the
runner refused rather than silently fitting on different bytes. The consequence,
however, is that the reported numbers can no longer be regenerated.

---

## Stage 1 — Target definition

| | |
|---|---|
| Purpose | Fix the prediction target before looking at evaluation outcomes |
| Daily task | A versioned production proxy: `PTS + 0.4*FG − 0.7*FGA − 0.4*(FTA−FT) + 0.7*REB + STL + 0.7*AST + 0.7*BLK − 0.4*TOV`. Explicitly **not** Hollinger Game Score |
| Transition task | Mean observed positive minutes over 30 calendar days after a supported move, censored strictly before any later supported move or waive |
| Transition contract frozen | SHA256 `863913cfa50bb35668b99a3354b6dfbec1c498e51a55acdd7a4218391dad555b`, approved **before** fitting |
| Status | **EXECUTED** |
| Evidence | `ENTRANT_MINUTES_PLAN.md`; `ABSTRACT.md` |

Freezing the target before fitting is what makes the later adverse result
reportable rather than something that could have been avoided by redefining the
outcome.

---

## Stage 2 — Population construction

| | |
|---|---|
| Daily | 79,358 observed records → **68,546** with complete history (86.38%). Exclusions driven by missing prior-season history |
| Transition | 1,569 trade legs → **313** evaluated episodes, 248 players, 49 issuance dates |
| Transition status ladder | 371 scored (incl. initial training), 450 draft consideration, 497 outside a unique regular-season range, 72 insufficient player history, 16 insufficient destination history, 43 ambiguous player/day, 16 ambiguous departure context, 104 no observed positive-minute outcome |
| Explicit honesty | The 104 unobserved outcomes are **not** labelled DNP, injured or zero minutes |
| Explicit limitation | The 313 are a **selected in-season population**; they do not represent all incoming players or offseason transactions |
| Status | **EXECUTED** |
| Evidence | `ENTRANT_MINUTES_RESULTS.md` status table |

---

## Stage 3 — Feature construction

| | |
|---|---|
| Daily features | Lagged ten-appearance mean; prior-season mean; home venue; log elapsed days |
| Transition features | Recent observed minutes; prior-season minutes; a 4-feature history ridge; a 12-feature history-plus-destination-context ridge |
| Training-only scaling | Yes — both ridge models scale on training data only |
| Regularization | Fixed alpha 1 for both ridge models |
| Prohibited and avoided | No score-driven tuning, no clipping, no model selection, no promotion |
| Status | **EXECUTED** |
| Evidence | `ENTRANT_MINUTES_PLAN.md` |

Feature counts matter here: the adverse transition result is a 12-feature model
versus a 4-feature model on only 58 training episodes in the first fold.

---

## Stage 4 — Evaluation design (past-only, cohort-aware)

| | |
|---|---|
| Daily split | Fit 2016-17..2022-23; evaluate 2023-24..2025-26. Coefficients frozen while histories update |
| Transition folds | Seven annual issuance folds beginning 1 July, 2018..2024. Each trained on earlier issues whose **entire target horizon has matured** |
| Shared episodes | All transition models are scored on the **same 313 episodes** |
| Block bootstrap | Daily: 5,000 resamples of seven-day calendar blocks |
| Cluster choice | Transition: clustered by player, and by issuance date as a sensitivity |
| Explicit limitation | All periods were previously available to development. **None is an untouched holdout** |
| Status | **EXECUTED** |
| Evidence | `ENTRANT_MINUTES_RESULTS.md`; `CONTEXT_AUDIT_RESULTS.md` |

Two design choices are load-bearing and are reported rather than buried:
the matured-horizon training rule, and the fact that the cluster choice changes
the transition conclusion.

---

## Stage 5 — Primary results

| Task | Result | Status |
|---|---|---|
| Daily | Context helps: MAE 5.1311 → 5.1158 (**0.30%**), paired −0.01529, interval [−0.02138, −0.01070] | **REPORTED** |
| Daily ablations | Rolling-ten 5.1625; elapsed-days 5.1163; home-only 5.1308 | **REPORTED** |
| Transition | History ridge MSE **41.555856**; context ridge **49.885811**; difference **+8.329955** | **REPORTED** |
| Transition intervals | Player-cluster **[3.124124, 14.211583]**; date-cluster **[−0.070992, 20.781618]** | **REPORTED** |

Both halves are reported with their intervals. The daily improvement is small but
consistent; the transition result is adverse and its sign depends on the
dependence assumption.

---

## Stage 6 — Failure localization

| Cohort | Finding | Status |
|---|---|---|
| Consecutive-day appearances | Context **reverses**: MAE 5.3137 → 5.3312 across 10,259 records | **REPORTED** |
| Episode direction | Context wins **148**, loses **165**; the single negative prediction is retained, not repaired | **REPORTED** |
| Issuance fold | Earliest fold = **96.45%** of net excess squared error (2018: 39.94 → 89.24) | **REPORTED** |
| Recent-minute bands | All four bands show worse context MSE: <10 (51), 10–<20 (107), 20–<30 (96), 30+ (59) | **REPORTED** |
| Departure context | Both present (296) and absent (17) groups adverse | **REPORTED** |
| >30-day gap cohort | 14 episodes, context/history 107.19/59.49 — **not** an injury cohort | **REPORTED** |

The fold-1 concentration is the most important localization: it points at
small-sample estimation, and the study explicitly declines to claim that as the
cause.

---

## Stage 7 — Controls

| Control | Result | Status |
|---|---|---|
| History ridge vs recent minutes | MSE difference −13.927245 | **REPORTED** |
| History ridge vs prior-season minutes | MSE difference −16.325916 | **REPORTED** |
| Fixed context penalty 10 / 100 / 1000 | MSE 44.509 / 41.469 / 41.275 | **POST_HOC**, descriptive only |
| Earlier-data selected policy | MSE **41.426** vs history 41.556; difference −0.129759, player-cluster 95% [−0.462062, 0.198816], date-cluster [−0.460530, 0.212727] | **POST_HOC**; **both intervals include zero** |
| Caveat | Secondary/post-hoc comparisons are exploratory, with no multiple-comparison correction | reported |

The history-only ridge is the strongest **predeclared** transition model. The
nested earlier-data selection lowers the transition error toward that baseline,
but it does not beat it: both cluster intervals include zero and the selected
policy's MAE is slightly worse. Fixed penalty candidates are descriptive and
cannot override the nested selection.
slightly lower point estimate than history, but reliable incremental benefit is
not established.

---

## Stage 8 — Reproduction and release

| | |
|---|---|
| Per-row prediction tables | **NOT COMMITTED** |
| Original input bytes | **MISSING** at the recorded hashes |
| Reproduction level achieved | **NONE** |
| Status | **BLOCKED** |
| Evidence | `REPRODUCTION_BLOCKER.md`, `REPRODUCTION_RECEIPT.json` |

This is the one stage that is not established, and it is why this repository must
not be presented as a reproducible artifact.

---

## Stage 9 — Not executed (follow-on studies)

Each of these is a distinct study with its own contract, not a claim of this paper:

- causal rest / travel / schedule effects
- participation and roster-membership forecasting
- injury modeling
- trade profitability, financial benefit, optimal trade timing
- coach/team context effects
- prospective issuance and verified available-at timing
- career-opportunity timing
- validation of any deployed system

---

## Summary

| Stage | State |
|---|---|
| 0 Data acquisition & vintage pinning | EXECUTED — and failed closed, which is the blocker |
| 1 Target definition | EXECUTED, contract frozen before fitting |
| 2 Population construction | EXECUTED, selection stated |
| 3 Feature construction | EXECUTED, no tuning or selection |
| 4 Evaluation design | EXECUTED, past-only, matured horizons, shared episodes |
| 5 Primary results | REPORTED, with intervals |
| 6 Failure localization | REPORTED, including the fold-1 concentration |
| 7 Controls & remediation | REPORTED, exploratory/post-hoc |
| 8 Reproduction & release | **BLOCKED** |
| 9 Follow-on studies | NOT EXECUTED |

**Eight of nine executed stages are sound. The ninth is blocked, and that is the
finding a reader most needs.**
