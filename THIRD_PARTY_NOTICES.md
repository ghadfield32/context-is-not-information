# Third-party attribution and terms

The package's software is licensed under the MIT licence. NBA data and
data-derived research artifacts have separate terms; the code licence grants no
rights to those materials.

## NBA.com

Statistics underlying this study originate from **NBA.com**. This statement is
attribution, not permission.

The tracked aggregates are derived research artifacts, not raw provider data.
Including them would be subject to a rights decision that has **not** been made
(see `RIGHTS.md`). No academic-intent, de-identification or affiliation exemption
is inferred.

## Transaction records

Two real-trade examples in the source study reference official NBA announcements.
Those links are citations for trade confirmation; the modeled numbers come from
the study's own predictions, not from the announcements.

## Bundled third-party data

**None.** This package bundles no raw box scores, player-game facts, team-game
facts, transaction records, or per-row derived evaluation tables. The original
inputs are private and, for the transition task, no longer present at the recorded
vintage (see `REPRODUCTION_BLOCKER.md`).

## Methodological precedents

Ridge regression, past-only evaluation, block bootstrapping, cluster-robust
intervals and context ablations are all established techniques. This package
claims no novelty for any of them. Its contribution is the paired evaluation and
its result, not the method.
