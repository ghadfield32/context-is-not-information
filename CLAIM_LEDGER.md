# DPV claim ledger

Every material claim in `abstract.txt`, bound to its evidence and its limitation.
Source artifacts live in the World Model Sports repository under
`docs/backend/projects/player_value/daily-player-value-decision-signals/`.

## Daily production task

| Claim | Evidence | Qualification |
|---|---|---|
| 68,546 evaluation appearances (86.38% of 79,358) | `ABSTRACT.md`; context audit aggregates | Exclusions driven by missing prior-season history. Observed-appearance conditioning: this is not a scheduled-opportunity denominator |
| MAE 5.1311 → 5.1158, a 0.30% reduction | `ABSTRACT.md`; `CONTEXT_AUDIT_RESULTS.md` | Retrospective. Coefficients frozen on 2016-17..2022-23 and evaluated on 2023-24..2025-26 |
| Paired difference −0.01529, interval [−0.02138, −0.01070] | 5,000 seven-day calendar-block resamples | Block bootstrap over calendar clusters; does not resolve source-availability questions |
| Rolling-ten 5.1625; elapsed-days 5.1163; home-only 5.1308 | Prespecified ablations on identical complete records | Prespecified, but descriptive comparisons on the same evaluation period |
| Improves in all three evaluation seasons | Season-level aggregation | All seasons were previously available to development; none is untouched |
| Reverses for consecutive-day appearances: 5.3137 → 5.3312 across 10,259 records | Consecutive-day cohort | A clearly identified failure cohort. It is **not** a causal rest effect |

## Transition task

| Claim | Evidence | Qualification |
|---|---|---|
| 313 evaluated in-season trade episodes, 248 players, 49 issuance dates | `ENTRANT_MINUTES_RESULTS.md` | Selected in-season population. Does **not** represent all incoming players or offseason transactions. 58 other scored rows initialize the first fit |
| History-only ridge MSE **41.555856** | Same table | Fixed alpha 1, training-only scaling, no score-driven tuning or model selection |
| Context ridge MSE **49.885811** | Same table | 12 features; the larger model is trained on only 58 episodes in fold 1 |
| Context-minus-history **+8.329955** | Primary contrast | Adverse. The evidence does not support promoting this model |
| Player-cluster 95% interval **[3.124124, 14.211583]** | 5,000 paired draws | Cluster choice materially changes the result |
| Issuance-date-cluster sensitivity **[−0.070992, 20.781618]** | Same draws, different clustering | **Dependence choice matters.** Retained rather than hidden |
| Context wins 148, loses 165 | Episode-level direction count | Counted, including the single negative prediction, which is not repaired after observing scores |
| First fold = **96.45%** of net excess squared error | Fold table (2018: history 39.94 vs context 89.24) | Localizes instability; does **not** prove small-sample estimation is the cause |
| History ridge beats recent (−13.93) and prior (−16.33) controls | Secondary comparisons | Exploratory, conditional on fitted models, no multiple-comparison correction |
| All four recent-minute bands show worse context MSE | Band table | <10 (51), 10–<20 (107), 20–<30 (96), 30+ (59) episodes |
| Post-hoc remediation ladder: fixed context penalties give MSE 44.509 (p10), 41.469 (p100), 41.275 (p1000) | `ENTRANT_SHRINKAGE_RESULTS.md` table | **Fixed candidates are descriptive.** They cannot override nested selection, and none of them is a selected policy |
| Earlier-data selected policy MSE **41.426** vs history **41.556**, difference −0.129759, player-cluster 95% [−0.462062, 0.198816], date-cluster [−0.460530, 0.212727] | Same results file | **Both intervals include zero and selected MAE slightly worsens.** Incremental benefit over the history baseline is **not established**. The first fold has one qualifying inner split, so it selects history-only |
| The >30-day gap cohort is **not** an injury cohort | 14 episodes, context/history MSE 107.19/59.49 | An injury interpretation would be unsupported |

## Explicitly not established

- Causal effects of rest, travel, or schedule.
- Participation, roster membership, or legal eligibility forecasts.
- Injury modeling.
- Trade profitability, financial benefit, or optimal trade timing.
- Coach/team context improving forecasts.
- Prospective issuance, historical available-at timing, or source authenticity.
- Validation of the deployed system.

## The reproduction boundary

The transition results are a **documented historical result**, not yet a
reproducible artifact. The original inputs no longer exist (see
`REPRODUCTION_BLOCKER.md`), the runner refuses on hash mismatch, and no per-row
prediction tables are committed. Any CSV of these aggregates would be a
transcription, not a reproduction, and would prove only internal consistency.
