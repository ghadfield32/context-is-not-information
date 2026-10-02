# What this system actually delivers

This file states, plainly, what the DPV context work establishes and what it does
not. Every item names its evidence and its limit. Nothing here is a claim of
financial or personnel benefit.

## The methodological benefit (established)

**A decision rule for admitting context features.**

> A context feature should not enter a player-value system because it is
> available. It should enter because it demonstrates incremental predictive value
> under the correct target, timing, cohort and sample size.

This is not a slogan. Both experiments apply it and both produce a non-obvious
answer:

| Experiment | Naive expectation | Measured outcome |
|---|---|---|
| Daily production | Adding venue and elapsed days helps | Helps **slightly** (0.30% MAE) but **reverses** in the consecutive-day cohort |
| Post-trade minutes | Richer destination context helps | **Hurts materially** (MSE 41.556 → 49.886) |

The benefit is the rule plus the demonstration that it changes conclusions.

## The diagnostic benefit (established)

**Failures are localized, not just reported.**

| Diagnostic | Finding | What it buys |
|---|---|---|
| Cohort split | Consecutive-day cohort reverses (5.3137 → 5.3312 on 10,259 records) | Tells a team *where* not to apply the adjustment |
| Cluster choice | Player-cluster interval excludes zero; date-cluster does not | Makes the dependence assumption an explicit part of the result |
| Episode direction | Context wins 148, loses 165 | Prevents "average improvement" from hiding a majority-losing model |
| Fold concentration | 96.45% of excess error in the earliest fold (58 training episodes) | Points at limited support as the likely mechanism |
| Band audit | All four recent-minute bands worsen | Rules out one subgroup driving the aggregate |
| Cohort caveat | The >30-day gap cohort is **not** an injury cohort | Prevents a tempting wrong interpretation |

## The engineering benefit (partially established)

**A hash-pinned pipeline that refuses to run on the wrong inputs.** The
transition runner refuses with `Source hash mismatch` rather than silently fitting
different bytes. That is why this paper cannot currently be reproduced — and it is
also evidence that the guard works. A pipeline that had not failed closed would
have produced numbers nobody could trace.

## The scientific benefit, bounded (established)

| Claim | Evidence | Limit |
|---|---|---|
| Context gains are small and cohort-dependent | 68,546 appearances; three seasons; interval [−0.02138, −0.01070] | Observed-appearance conditioning; not a scheduled-opportunity denominator |
| Player history is a strong transition baseline | History ridge MSE 41.556 beats recent (−13.93) and prior (−16.33) controls | Exploratory comparisons, no multiple-comparison correction |
| Richer context can be actively harmful | +8.330, player-cluster [3.124, 14.212] | Selected in-season population, 313 episodes |
| The harm is localized, not explained | Fold-1 share 96.45% | Small-sample estimation is a hypothesis, not a proven cause |
| Remediation does not yet beat history | Nested selected 41.426 vs 41.556; both intervals include zero | Post hoc; requires a prospective test |

## What is explicitly NOT delivered

- **No financial benefit.** Not measured, not claimed.
- **No trade profitability or optimal trade timing.** Forecast error is not
  personnel-decision value.
- **No participation or availability forecast.** Who plays is a separate problem.
- **No injury modeling.** The >30-day cohort is not an injury cohort.
- **No causal rest, travel or schedule effect.** These are associations.
- **No coaching or team-context effect.**
- **No validated deployed system.**
- **No confirmed incremental gain** from shrinkage or support restriction over the
  history baseline.

## The honest summary

The system's demonstrated benefit is **diagnostic and methodological**: it tells a
team *when* a plausible context feature is worth adding, and it shows that the
answer can be "no" even when the feature sounds obviously useful.

Turning that into a decision or financial benefit is a separate study that has not
been run.
