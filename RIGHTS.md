# Rights and data disposition — DPV

**Status: no redistribution licence is asserted, and none was obtained.**

## What is claimed

| Material | Position |
|---|---|
| Original WMS code | MIT, covering original code only |
| NBA-derived data and derived aggregates | **No licence asserted.** Attribution to NBA.com is required and does not grant redistribution rights |
| Raw box scores, player-game facts, team-game facts, transaction records | **Not bundled.** Private inputs |
| Derived aggregate reports | Present as reported results; their redistribution is an **open decision** |

## What is not claimed

- That the authors hold a licence to redistribute NBA-derived content.
- That anonymizing player and episode identifiers changes the rights position. **It
  does not.** De-identification is not a licence, and this package does not treat
  it as one.
- That academic intent, a public repository URL, or the MIT code licence grants
  third-party data rights.
- That this repository has been legally reviewed.

## The decision that is required

Sloan asks for the data used in the research and places third-party permission
responsibility on the author. This study's inputs are NBA-derived and its
original input bytes are missing, so the package currently supplies **neither**
bundled data nor a working acquisition route.

The operator must choose, explicitly:

1. **Bundle derived evaluation data** — requires a rights position the operator is
   willing to accept, and requires the data to exist in reproducible form first.
2. **Supply a pinned acquisition route** — not currently possible, because the
   original vintage is unavailable.
3. **Publish code and reported results only**, with the reproduction limitation
   stated plainly and the repository **not** presented as a reproducible artifact.

Option 3 is the honest description of the current state, and it is what
`README.md` and `DATA.md` say.

## Do not

- Do not add an anonymization disclaimer that implies the rights question is
  resolved by de-identification.
- Do not describe this package as reproducible while the inputs are missing.
- Do not copy private source tables into a public repository at a deadline.
