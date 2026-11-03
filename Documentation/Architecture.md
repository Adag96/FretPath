# Architecture

The planned agent pipeline, with the KBAI technique behind each stage. This describes the intended design, not built code. Update it as stages are built.

## Pipeline

| Stage | What it does | KBAI technique |
|---|---|---|
| 1. Represent | Model the fretboard, notes, chords, voicings, and finger assignments | Frames, semantic networks |
| 2. Generate voicings | Enumerate fret combinations that cover a chord's tones | Generate & test (generator) |
| 3. Test playability | Reject voicings that break hard rules: fret span, finger count, string gaps, muted strings | Generate & test (tester), production rules |
| 4. Seed from known shapes | Start from familiar shapes (open chords, E/A barre, CAGED) and transpose them | Case-based reasoning |
| 5. Score transitions | Cost of moving between two voicings: anchor fingers, position shift, barre changes, voice leading | Production rules |
| 6. Sequence | Find the lowest-cost path through the progression (one voicing per chord) | Search, means-ends analysis, planning |
| 7. Explain | Report why each voicing was chosen and which fingers stay anchored | Explanation |
| 8. Personalize (later) | Learn which voicings and transitions Adam finds comfortable from feedback | Incremental concept learning, recording cases |

## Open design questions

- Data format for a voicing: fret per string plus finger per string?
- Hard constraints (stage 3) versus soft costs (stage 5): where does each rule belong?
- How many voicings per chord to keep before searching, and should weak ones be pruned early?
- Input format for progressions: chord symbols like `G C Em D`?
