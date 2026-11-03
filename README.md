# FretPath

A knowledge-based agent that picks guitar fingerings for a whole chord progression, not just one chord at a time.

Chord charts show one shape per chord. When you're playing a progression, the best shape for each chord depends on the chords around it: shared fingers, small hand movements, and smooth voice leading. FretPath searches the possible voicings and suggests the sequence that is easiest to play, with an explanation of each choice.

> **Status:** early development. Nothing is usable yet.

## How it works (planned)

1. **Represent** the fretboard, chords, voicings, and finger positions.
2. **Generate** candidate voicings for each chord, then test them against playability rules such as fret span, barres, and muted strings.
3. **Score** each transition using ergonomic rules, for example a finger that stays put between chords costs almost nothing.
4. **Search** for the lowest-cost path through the progression.
5. **Explain** the result: why each voicing was chosen and which fingers anchor each change.

## Requirements

- Python 3.13+

## Development

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
python -m unittest discover tests
```

## License

MIT. See [LICENSE](LICENSE).
