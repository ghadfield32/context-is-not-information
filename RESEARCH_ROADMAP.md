# DPV research roadmap

The long-term Player Value system is broader than the submitted paper. This file
keeps the dependency order explicit so later engineering does not silently
upgrade a research claim.

## Phase A — Close the submitted evidence package

1. Recover or replace the historical reproduction route.
2. Retain row-level evaluation evidence for future experiments.
3. Move rights-cleared data/evidence into this standalone repo.
4. Add a clean-clone reproduction script.
5. Add deterministic tests for every published number.

## Phase B — Historical trajectory study

### H0 — history

Reproduce the existing history model exactly.

Gate:

[
max |hat y_{H0,new} - hat y_{H0,parent}| le epsilon.
]

If H0 does not reproduce, stop.

### H1 — workload trajectory

Add genuinely ordered deployment information such as:

- recent minutes slope;
- rotation-share slope;
- starts/bench transition;
- persistence of the current workload regime;
- workload variability or change-point indicators.

Do not add an algebraic transform of existing H0 fields and call it new
information.

### H2 — production trajectory

Add ordered production dynamics such as:

- production-rate slope;
- usage trend;
- shot-volume trend;
- efficiency trajectory;
- playmaking trajectory.

Primary metric remains transition MSE. Also report RMSE, MAE, bias, P90 and P95,
with both player and issuance-date dependence analyses.

## Phase C — Prospective career/opportunity experiment

Keep the existing prospective design distinct from H0/H1/H2.

### C0

History.

### C1

Career-transition state:

- age relative to role-specific career state;
- experience/service;
- workload change;
- dated role movement.

### C2

C1 plus role-specific opportunity:

- departed overlapping workload;
- incumbent competition;
- simultaneous arrivals;
- complementary arrivals;
- coach-role affinity;
- health-adjusted competition.

Do not fit C0/C1/C2 until required source roles have real
`available_at <= issuance` evidence.

## Phase D — Participation

Estimate:

[
P(A=1 | I).
]

Risk-set states should distinguish at least:

- eligible active;
- eligible DNP;
- injured;
- inactive;
- suspended;
- not on roster;
- unknown/source missing.

Primary metrics: log loss, Brier score and calibration.

## Phase E — Conditional workload and production

Estimate separately:

[
E[M | A=1,I]
]

and

[
E[R | A=1,M,I].
]

Then evaluate total contribution rather than multiplying independently optimized
point estimates without joint validation.

## Phase F — Joint rotation

Model player participation and minutes jointly subject to actual team game
duration:

[
sum_i M_i = T_g.
]

This is where incoming opportunity, incumbent displacement, health, role
competition and coach deployment become one coherent forecast.

## Phase G — Team and decision state

Feed accepted player/rotation distributions into a future-team model.

Only then compare actions such as:

- retain;
- deploy differently;
- extend;
- trade;
- wait.

Every alternative must use the same information cutoff and horizon.

Forecasting a traded player's destination minutes is not equivalent to showing
that the trade was the best available action.

## Phase H — Contracts, picks and economics

After the basketball decision layer is qualified, add:

- contract control;
- cap/tax state;
- pick rights and protections;
- package legality;
- replacement deployment.

Keep economic outputs separate by stakeholder. A team salary payment and player
salary receipt are transfers, not newly created combined wealth.

## Required evidence state on every feature

Every feature should carry:

- definition;
- unit;
- grain;
- source generation;
- available-at timestamp;
- intended model consumer;
- forecast target;
- evidence status.

Use one of:

- `QUALIFIED_INPUT`;
- `RETROSPECTIVE_ONLY`;
- `EXPLANATION_ONLY`;
- `BLOCKED`.

## Research principle

The system grows only when a new information block demonstrates incremental
value for the correct estimand and timing. Architecture complexity is not itself
evidence.
