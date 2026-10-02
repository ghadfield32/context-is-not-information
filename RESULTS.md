# Results summary

This page separates the submitted primary results from later diagnostics and
planned extensions.

## 1. Daily next-appearance production

Population:

- 79,358 observed records;
- 68,546 with complete history used in the common evaluation cohort;
- evaluation seasons 2023-24 through 2025-26;
- coefficients fit on 2016-17 through 2022-23.

Primary comparison:

| Forecast | MAE |
|---|---:|
| Player history | 5.1311 |
| Player history + simple daily context | **5.1158** |

Difference:

- context-minus-history MAE = **-0.01529**;
- relative reduction ≈ **0.30%**;
- seven-day block-bootstrap 95% interval = **[-0.02138, -0.01070]**.

The point estimate improves in all three evaluation seasons.

### Failure cohort

For 10,259 consecutive-day appearances:

| Forecast | MAE |
|---|---:|
| Player history | **5.3137** |
| Player history + daily context | 5.3312 |

The average gain therefore does not generalize uniformly across short-rest
appearances. This is not a causal rest-effect estimate.

## 2. Post-trade conditional minutes

Evaluated support:

- 313 in-season transition episodes;
- 248 players;
- 49 issuance dates;
- seven expanding earlier-only evaluation cohorts.

Primary comparison:

| Forecast | MSE |
|---|---:|
| Recent observed minutes | 55.48 |
| Prior-season observed minutes | 57.88 |
| **History-only ridge** | **41.56** |
| History + destination context ridge | 49.89 |

Primary context contrast:

- context-minus-history MSE = **+8.33**;
- player-cluster 95% interval = **[3.12, 14.21]**;
- issuance-date-cluster sensitivity = **[-0.07, 20.78]**;
- context improves 148 episodes and worsens 165.

### Failure localization

The earliest evaluation fold contributes **96.45%** of the net excess squared
error and trains the larger context model on only **58 episodes**.

That localizes instability but does not establish its cause.

## 3. Post-hoc transition remediation

These are diagnostics, not confirmatory primary results.

| Forecast | MSE | Interpretation |
|---|---:|---|
| History-only ridge | 41.56 | Strong predeclared baseline |
| Rich destination context | 49.89 | Material degradation |
| Support-aware fallback | 43.94 | Removes some damage; still worse than history |
| Shrinkage | 41.43 | Removes nearly all damage; reliable incremental gain not established |

The scientifically useful conclusion is not that "context never works." It is
that richer context needs correct support, timing, estimand and regularization
before it can be trusted to improve a strong history baseline.

## 4. Additional retrospective evidence

Other retained DPV studies provide supporting context for the full manuscript:

- advanced metrics: approximately **0.11%** MAE improvement on a narrower
  30,905-appearance subset with about 38.94% coverage;
- annual/career forecasting: approximately **6.96%** lower retrospective MAE
  than persistence on 2,245 matched player-seasons.

These are not primary submitted-abstract results and should remain clearly
separated until their exact evidence packages are incorporated into this
standalone repository.

## 5. What is not a result yet

The following remain research questions:

- whether workload trajectory improves transition forecasting;
- whether production trajectory adds value beyond workload trajectory;
- whether career/opportunity features improve prospectively;
- participation probability;
- coherent joint rotations;
- trade-action counterfactuals;
- financial outcomes.

See `RESEARCH_ROADMAP.md`.
