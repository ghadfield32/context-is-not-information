# Reproduction guide

## Current status

The submitted numerical results are traceable to retained study documents, but
the historical transition experiment is **not currently reproducible end to
end from this standalone repository**.

That limitation is structural, not cosmetic.

Two exact historical inputs are no longer present at the hashes used by the
transition run:

- `player_game_fact.parquet`;
- `team_game_fact.parquet`.

A later vintage exists, but rerunning on different bytes would define a new
experiment rather than reproduce the historical result.

No per-row target/prediction table was retained for the historical transition
study.

See `REPRODUCTION_BLOCKER.md` for exact hashes.

## What can be checked now

A reader can currently audit:

1. the abstract;
2. the claim ledger;
3. the population and model definitions;
4. the reported primary and sensitivity statistics;
5. the documented input hashes and mismatch;
6. the distinction between primary, secondary, post-hoc and planned claims.

The current package therefore supports **claim traceability**, not end-to-end
forecast reproduction.

## What will close the transition reproduction gap

The preferred closure is:

1. recover the two historical parquet files at their recorded SHA-256 hashes;
2. rerun the frozen historical transition pipeline;
3. retain an episode-level public evidence table containing only fields needed
   for evaluation:
   - anonymous episode id;
   - anonymous player id;
   - evaluation fold;
   - clustering keys;
   - target;
   - recent-minutes prediction;
   - prior-season prediction;
   - history-ridge prediction;
   - context-ridge prediction;
4. recompute the primary MSE contrast and both cluster sensitivities;
5. reproduce the 148/165 direction count and the fold-1 excess-error share;
6. review the public evidence table for data rights/privacy;
7. verify the package from a clean clone.

## Daily-task closure

The daily task should be similarly rebuilt from a pinned historical box-score
vintage and should retain a minimal evaluation table sufficient to recompute:

- common-cohort size;
- history MAE;
- context MAE;
- seven-day block-bootstrap contrast;
- season-level results;
- consecutive-day cohort.

## New studies must not overwrite the historical result

If the exact historical transition inputs cannot be recovered, use a new,
explicitly versioned data vintage and report the new experiment as a new result.

Do not:

- overwrite historical hashes;
- relabel a later vintage as the old one;
- transcribe aggregate results into a table and call that reproduction.

## Development branch

This branch may add new experiments. Each new experiment should include:

- frozen contract;
- source manifest;
- exact data vintage;
- fit/evaluation cutoffs;
- model/config identity;
- per-row retained predictions where rights permit;
- aggregate metrics;
- uncertainty;
- adverse cohorts;
- reproduction receipt.
