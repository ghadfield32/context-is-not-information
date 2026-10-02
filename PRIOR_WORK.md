# Prior work and the novelty boundary

The study does not claim to invent context-aware player forecasting, ridge
regression, or past-only evaluation. Adding schedule, venue and team context to
player models is established practice across public NBA analytics.

## What is not claimed

- Not the first use of rest, travel or venue features in NBA forecasting.
- Not a new estimator. The models are ordinary least squares and fixed-alpha ridge.
- Not a new dataset.
- Not a causal design.

## The bounded contribution

A **paired, same-episode comparison under past-only, cohort-aware evaluation**
that tests whether context features earn their place, and finds:

1. **A small real gain in routine forecasting** — 0.30% MAE, detectable across
   three evaluation seasons on 68,546 appearances.
2. **A reversal in a specific short-rest cohort** — the gain does not hold for
   consecutive-day appearances.
3. **A substantial adverse result under transition** — richer destination context
   raises conditional-minutes MSE by 8.33 on 313 episodes, losing on more episodes
   than it wins.
4. **A localized instability rather than a mechanism** — 96.45% of the excess
   error is in the earliest fold, which the study reports instead of tuning away.
5. **A dependence-choice sensitivity** — the player-cluster interval excludes zero
   while the issuance-date-cluster interval does not. The study reports both.

## Companion results in the same program

- **PMI** — *a rating is not a forecast*
- **E1** — *more measured state is not automatically more information*
- **DPV** — *context is not automatically information*

These are independent studies with independent data and evaluation contracts.
They share a thesis about assuming that more inputs means more information; none
of them claims the others.

## Required before a stronger claim

A claim that this context model is harmful in general would need larger transition
samples, frozen partial pooling, nested earlier-only selection, and a genuinely
prospective evaluation. Small-sample instability is localized here, not explained.
