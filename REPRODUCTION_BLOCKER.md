# Historical reproduction blocker

The historical transition experiment is **not currently reproducible end to end
from this repository**.

## Exact blocker

Two of the three hash-pinned historical inputs are no longer present at the
bytes used by the study:

| Input | Historical SHA-256 | Current retained bytes |
|---|---|---|
| `player_game_fact.parquet` | `368dbee5fb6aaf027d9268521e64c34c45cd50a7dd77c4579b2dedf965da032e` | `a9364e6f01c03854b125e35177d017e4906c11de6b01c9f0257634368512488d` |
| `team_game_fact.parquet` | `48b16b979f01121ca2c5dd0bdb1afb1ea13b89036b1da63cb0a77c273e52bd03` | `199ad56ce16a08a95b2449f599204d8292f4b41dda668bb72ec99a940fe91904` |
| `transaction_events.parquet` | `bafd95455af3fc4600461c4941a17dc6ebe82a2967422559c42ac8966dd32744` | unchanged |

The frozen runner correctly refuses a source-hash mismatch rather than silently
fitting against a different vintage.

A bounded retained-file search found no exact copy of the two missing
historical inputs. That is evidence about the searched archive, not proof that
no external copy exists anywhere.

## Why a later vintage is not a reproduction

A separately declared later vintage exists, but its bytes differ. Refitting on
those files would produce a new experiment and cannot be labeled reproduction
of the historical result.

## Why aggregate transcription is not enough

No episode-level table containing targets and model predictions was retained.
Copying aggregate report values into a CSV would only show that arithmetic on
the reported values is internally consistent; it would not show that the
forecasting pipeline produced them.

## Closure criteria

1. Recover the two historical parquet files at the original hashes, or recover a
   verified equivalent copy.
2. Re-run the frozen transition pipeline.
3. Retain a rights-reviewed episode-level evaluation table with clustering keys,
   target and all compared predictions.
4. Recompute primary MSE, both cluster sensitivities, win/loss counts and fold
   concentration.
5. Reconstruct the daily task from a pinned historical box-score vintage.
6. Verify the complete package from a clean clone.

Until then, describe the transition result as a documented historical result,
not an independently reproducible public experiment.
