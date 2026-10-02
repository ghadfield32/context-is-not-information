# Scientific source inventory

This inventory identifies the exact monorepo source files associated with the
current DPV paper and its transition diagnostics.

Source repository:

`ghadfield32/betts_basketball`

Source main commit recorded for this inventory:

`adbc4e1b517303deed2ed0134bf869f42f28ef67`

The standalone DPV repository does **not** yet vendor this code because the
historical runners depend on shared research helpers and monorepo package
structure. Copying only a subset would create a misleading "standalone" package.

## Core transition source

| Monorepo path | Git blob SHA | Role |
|---|---|---|
| `scripts/nba_value/research/entrant_minutes.py` | `00abba2718303b412a4cade02b6b64669a784ac1` | Episode construction and primary history/context models |
| `scripts/nba_value/research/entrant_minutes_run.py` | `5803007db143c900e8ae2aeb27ece80b9a992a0c` | Frozen historical transition runner |
| `scripts/nba_value/research/entrant_shrinkage.py` | `1fcdf07aa693fc709185b0e8e76f2d8b70b1c6af` | Post-hoc shrinkage diagnostic |
| `scripts/nba_value/research/entrant_coverage.py` | `51952c0da1ee7aedd84f3e08daa1d39a05ddeb1f` | Coverage/support diagnostics |
| `scripts/nba_value/research/entrant_diagnostic.py` | `5e03add9e42c08bfb167390577c0bff3e8a71f2d` | Transition diagnostic helpers |
| `scripts/nba_value/research/entrant_direction.py` | `2e6fc88caff8b9fefe14c9a5d9826fd80502bde3` | Direction/source audit |
| `scripts/nba_value/research/context_run.py` | `0d20a5eca4e99ea6642356884dc4144a1ab78978` | Matched-error and reconstructed-context runner |
| `scripts/nba_value/research/context_audit.py` | `db0099c20cd2625e7fd3d6dda8788e4bea2ea2bb` | Error grouping and context diagnostics |

## Shared research helpers

| Monorepo path | Git blob SHA | Role |
|---|---|---|
| `scripts/nba_value/research/artifacts.py` | `46c03d670ae28fbaa83426586467b0019d9d862a` | Generation hashing/sealing |
| `scripts/nba_value/research/factor_use_receipt.py` | `8e63fe97b62a5b0e8ed9277b4402b6ade488576d` | Checked source reads and saved-prediction inspection |
| `scripts/nba_value/research/supplement.py` | `14514b8db0cd4f8e843fc35213f91a476a2e2c5b` | Cluster intervals and supplementary metrics |
| `scripts/nba_value/research/trade_replay.py` | `7cbe6bf6ef64fc7d7c4e8f4dfca3e36df147715e` | Canonical IDs and historical trade replay helpers |

Additional dependencies referenced by these modules still need a closed
standalone inventory before vendoring.

## Key tests

| Monorepo path | Git blob SHA |
|---|---|
| `tests/unit/test_dpv_entrant_minutes.py` | `b8b4d656e520be0460b6f3e841e1971c1d659e21` |
| `tests/unit/test_dpv_entrant_shrinkage.py` | `3bd4af7ea346ab78605ec1c3ed318a37dc097d64` |
| `tests/unit/test_dpv_entrant_coverage.py` | `42fd011a436094a5f9ae5a90b6fd1818e8652331` |
| `tests/unit/test_dpv_entrant_direction.py` | `d336869b68038d05235292cd7976706b46e37378` |

## Key study documents

| Monorepo path | Git blob SHA |
|---|---|
| `docs/backend/projects/player_value/daily-player-value-decision-signals/ENTRANT_MINUTES_PLAN.md` | `ca773272756104c8506597eec0cffa5544e53ab5` |
| `docs/backend/projects/player_value/daily-player-value-decision-signals/ENTRANT_MINUTES_RESULTS.md` | `5230a52d9207b717db66aefa8eeb92dadd00317c` |
| `docs/backend/projects/player_value/daily-player-value-decision-signals/ENTRANT_SHRINKAGE_PLAN.md` | `ff6280748eb70bad19d953ff8479e68cd4b4f1ee` |
| `docs/backend/projects/player_value/daily-player-value-decision-signals/ENTRANT_SHRINKAGE_RESULTS.md` | `46a8e168cabcacff86ca614b79f18ced5eb4fd08` |

## Existing retained daily-study reports

The monorepo also retains versioned report generations under:

`reports/research/daily_player_value/`

including the September 30 daily release, advanced-metric release, transition
calibration, stage-value reports and regime evidence.

These reports are useful provenance, but they should not be bulk-copied into the
standalone repo until each artifact is classified as:

- needed for a public claim;
- rights-cleared;
- free of private paths or private row-level data;
- version-bound to the manuscript.

## Standalone extraction gate

Before copying scientific source into this repository:

1. close the Python import/dependency graph;
2. copy only the minimal scientific modules and tests;
3. replace monorepo-root assumptions with a standalone package boundary;
4. preserve numerical behavior with regression tests;
5. bind the exact source blobs above in a migration manifest;
6. run source-only tests before and after extraction;
7. run the historical experiment only if the exact data vintage is available;
8. never weaken source-hash checks to make the extraction pass.

Until then, this file is the source-lineage authority for the standalone paper.
