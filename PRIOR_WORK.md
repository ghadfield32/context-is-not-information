# Prior work and novelty boundary

This study does not claim to invent context-aware player forecasting, ridge
regression, player-history models, or past-only evaluation.

## What is not claimed

- Not the first use of rest, travel, venue, roster or team context in basketball analytics.
- Not a new estimator; the core models use ordinary least squares and fixed-alpha ridge.
- Not a new causal design.
- Not evidence that more context is harmful in every forecasting setting.

## Bounded contribution

The current evidence contributes a paired, cohort-aware test of whether
additional context earns inclusion beyond player history.

The central findings are:

1. a small average gain from simple daily context;
2. a reversal of that gain in a consecutive-day cohort;
3. a strong history-only conditional-minutes baseline across roster transitions;
4. material degradation from a richer destination-context specification;
5. dependence-sensitive uncertainty;
6. failure localization in the earliest, smallest-support fold; and
7. post-hoc evidence that support restrictions and shrinkage remove much of the
   damage without establishing reliable incremental improvement over history.

The contribution is therefore methodological and applied:

> contextual variables should be admitted only after demonstrating incremental
> predictive value under the correct estimand, information timing, population
> and dependence structure.

## Stronger claims require stronger evidence

A claim that a particular context model improves transition forecasting would
need, at minimum:

- a frozen context specification;
- larger and better-supported transition samples;
- retained row-level predictions;
- exact source-vintage lineage;
- earlier-only model selection where applicable;
- prospective evaluation;
- reproduction from a clean public package.

The current historical evidence motivates those tests but does not substitute
for them.
