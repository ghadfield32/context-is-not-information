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

## Package integrity: check this first

Package integrity is separate from scientific reproduction, and unlike the
forecast reproduction it **does** hold today. Verify it from a clean clone:

```bash
git clone --branch full-paper-development \
    https://github.com/ghadfield32/context-is-not-information.git
cd context-is-not-information
python verify_integrity.py
```

The script exits non-zero unless every check passes:

1. every entry in `SHA256SUMS` matches the file it names;
2. `SHA256SUMS` lists every tracked file except itself;
3. `GIT_MANIFEST.json` maps every tracked blob to a `git hash-object` digest;
4. the two files agree about each other;
5. `snapshot_base_commit` resolves to a real commit in the repository;
6. the retracted values do not reappear as results (each surviving mention is
   a documented retraction, not an assertion).

### Why the check must run against a clone

`.gitattributes` declares `* text=auto eol=lf`. On a Windows checkout the
worktree can hold CRLF bytes while Git stores LF, so a checksum computed from
the worktree describes bytes no clone will ever receive. That happened on this
branch and was invisible locally: six entries verified on the authoring machine
and failed on a clean clone. Hashes recorded here describe **committed** bytes.

### Declared exclusions

Neither integrity file can record the hash of the commit containing it, so both
describe `snapshot_base_commit` and are committed in that commit's child.

- `SHA256SUMS` excludes only itself, matching the PMI and E1 packages.
- `GIT_MANIFEST.json` excludes itself and `SHA256SUMS`. The latter is not
  optional: `SHA256SUMS` records this file's sha256, so including it would make
the pair unsatisfiable. An earlier revision did include it and one entry was
permanently stale.

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
