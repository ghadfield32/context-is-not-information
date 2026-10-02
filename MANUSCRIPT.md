# Context Is Not Information: Testing Daily and Transition Signals in NBA Player Forecasting

**Geoffrey Hadfield**  
World Model Sports LLC

## Abstract

See `abstract.md` for the submitted abstract. The branch
`submitted-abstract-2026-10-01` preserves the exact submitted repository state.

---

## 1. Introduction

Player-value systems are often improved by adding context: rest, venue, team,
role, opponent, health, coaching, roster state, or transition conditions. The
intuition is appealing: a richer description of the environment should make a
forecast more informed.

That intuition is not sufficient.

Additional variables can be mistimed, weakly supported, redundant with player
history, conditioned on the wrong population, or too flexible for the available
sample. Context can therefore reduce forecast quality even when every feature
has an intuitive basketball interpretation.

This paper asks:

> **When does additional context actually improve an NBA player forecast, and
> when does it make the forecast worse?**

We study two retrospective forecasting settings:

1. next-appearance production, where simple daily context is added to recent and
   prior-season player history; and
2. post-trade conditional minutes, where player-history forecasts are compared
   with a richer destination-context model.

The two settings produce a useful contrast. Simple daily context has a small
average benefit, but that benefit reverses in a consecutive-day cohort.
Transition context performs materially worse than a strong history-only model.
Post-hoc support restrictions and shrinkage reduce the transition damage but do
not establish robust incremental improvement over history.

The central claim is therefore procedural rather than architectural:

> **Context should earn inclusion through temporally valid, cohort-aware
> incremental evaluation. It should not be admitted merely because it is
> available or intuitively relevant.**

This paper does not claim causal rest effects, prospective personnel value,
trade profitability, or financial benefit.

## 2. Research questions

### RQ1 — Routine forecasting

Does simple daily context improve next-appearance production beyond player
history?

### RQ2 — Failure cohorts

Are there identifiable populations where the average context gain reverses?

### RQ3 — Roster transitions

Does richer destination context improve post-trade conditional-minutes forecasts
beyond player history?

### RQ4 — Failure remediation

When context hurts, can support restrictions or shrinkage reduce the damage
without overstating evidence of improvement?

### RQ5 — Evidence discipline

What evidence must exist before a contextual signal can be promoted from a
descriptive explanation to a forecasting input or personnel-decision input?

## 3. Data and targets

### 3.1 Daily production task

The target is a fixed, versioned box-score production proxy:

[
PTS + 0.4FG - 0.7FGA - 0.4(FTA-FT) + 0.7REB + STL + 0.7AST + 0.7BLK - 0.4TOV.
]

It is not Hollinger Game Score.

The common evaluation cohort contains 68,546 appearances with complete history
out of 79,358 observed records. The model is fit on 2016-17 through 2022-23 and
evaluated on 2023-24 through 2025-26.

### 3.2 Transition task

The transition target is mean observed positive minutes over a 30-calendar-day
destination horizon, censored before a later supported move or waive.

The scored historical evaluation contains:

- 313 episodes;
- 248 players;
- 49 issuance dates;
- seven expanding annual issuance folds.

This population is conditional on observed positive-minute destination
appearances. It does not represent all roster opportunities, inactive players,
or offseason transitions.

## 4. Forecasts

### 4.1 Daily history and context

The daily task uses:

- lagged ten-appearance history;
- prior-season history;
- home venue;
- log elapsed days.

Coefficients remain frozen while player histories update through evaluation.

### 4.2 Transition baselines

The transition task compares:

- recent observed minutes;
- prior-season observed minutes;
- a four-feature history-only ridge model;
- a twelve-feature history-plus-destination-context ridge model.

Both ridge models use fixed regularization and training-only scaling.

## 5. Evaluation

Daily paired uncertainty uses 5,000 resamples of seven-day calendar blocks.

Transition uncertainty uses paired player-cluster resampling, with
issuance-date clustering as a sensitivity.

All models in a transition comparison are scored on the same episodes.

No evaluation period is claimed as a fresh untouched holdout. Historical source
availability is not established as an authenticated issuance-time record.

## 6. Results

See `RESULTS.md` for the compact numerical tables.

### 6.1 Small average daily gain

Simple daily context lowers MAE from 5.1311 to 5.1158. The paired change is
-0.01529, with a seven-day block-bootstrap 95% interval of
[-0.02138, -0.01070].

The effect is small: approximately 0.30%.

### 6.2 A clear short-rest reversal

Across 10,259 consecutive-day appearances, context increases MAE from 5.3137 to
5.3312.

This is a failure cohort, not evidence that rest causally changes performance.

### 6.3 Player history transfers better than naive destination context

In 313 transition episodes, the history-only ridge reaches MSE 41.56 while the
richer destination-context ridge reaches 49.89.

The context-minus-history difference is +8.33. The player-cluster 95% interval
is [3.12, 14.21]. Under issuance-date clustering the interval broadens to
[-0.07, 20.78], demonstrating that dependence assumptions matter.

Context improves 148 episodes and worsens 165.

### 6.4 The failure is localized, not explained

The earliest transition fold contributes 96.45% of the net excess squared
error. That fold trains the larger context model on only 58 episodes.

This pattern is consistent with instability from limited support, but the study
does not claim that small sample size is the proven mechanism.

### 6.5 Post-hoc remediation

A support-aware fallback reduces MSE from 49.89 to 43.94. Shrinkage reduces it
to 41.43.

These are useful diagnostics. They show that context damage can be reduced by
restricting unsupported behavior and shrinking toward a strong history model.
They do not establish robust superiority over the 41.56 history-only baseline.

## 7. Interpretation

Three findings matter.

First, context can have genuine but small value in a routine forecasting regime.

Second, that value can reverse in a specific cohort, so a pooled gain should not
be treated as universal.

Third, adding a larger context block during roster transitions can materially
degrade performance relative to player history. The natural response is not to
search indefinitely for a context specification that wins on the same exposed
sample. It is to identify the missing estimands and test them separately.

This motivates a decomposition:

[
Career ightarrow Opportunity ightarrow Participation ightarrow Workload
ightarrow Production ightarrow Rotation ightarrow TeamState ightarrow Decision.
]

Each layer should be admitted only after demonstrating incremental value for its
own target under the correct information cutoff.

## 8. Additional evidence for the full paper

Retained DPV studies also suggest:

- advanced metrics add only a small incremental production-forecast gain on
  narrower coverage;
- structured career history can improve longer-horizon retrospective forecasts;
- support-aware routing reduces context damage without defeating the history
  baseline;
- shrinkage can nearly eliminate the measured context penalty.

These should be incorporated only with their exact evidence packages and claim
status.

## 9. Limitations

1. The daily task conditions on observed appearances.
2. The transition target conditions on positive-minute destination outcomes.
3. Historical source availability is not authenticated as pregame/issuance-time
   availability.
4. No submitted-period result is an untouched prospective holdout.
5. Transition support is modest and dependence assumptions affect uncertainty.
6. The historical transition run is not independently reproducible from this
   standalone repository because two exact input files are unavailable and no
   per-row prediction table was retained.
7. Forecast accuracy does not establish trade-decision value, causal effects, or
   financial benefit.

## 10. Reproducibility and evidence status

See:

- `REPRODUCE.md`;
- `REPRODUCTION_BLOCKER.md`;
- `REPRODUCTION_RECEIPT.json`;
- `CLAIM_LEDGER.md`;
- `SCIENTIFIC_STATUS.md`.

The repository intentionally refuses to substitute a later data vintage for the
historical one and call that a reproduction.

## 11. Next experiments

The next development study is a nested historical test:

- **H0:** player history;
- **H1:** H0 + ordered workload trajectory;
- **H2:** H1 + ordered production trajectory.

A separate prospectively registered study keeps career-state and
role-opportunity features distinct and remains blocked until its source
qualification requirements are met.

Participation, joint rotation, trade alternatives and economics remain later
research layers.

See `RESEARCH_ROADMAP.md`.

## 12. Conclusion

The evidence does not support a simple rule that more context improves player
forecasting. Simple daily context adds a small average signal but fails in a
clear cohort. Richer destination context substantially worsens a transition
forecast unless its behavior is constrained or shrunk back toward history.

The practical standard is therefore stronger than feature availability:
context should enter a player-value system only after demonstrating incremental,
temporally valid predictive value for the correct estimand and population.
