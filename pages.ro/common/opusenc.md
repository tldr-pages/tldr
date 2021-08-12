# opusenc

> Conversia audio WAV sau FLAC în Opus.
> Mai multe informaţii: <https://opus-codec.org/docs/opus-tools/opusenc.html>

- Conversia WAV la Opus utilizând opțiunile implicite:

`opusenc {{path/to/input.wav}} {{path/to/output}}.opus`

- Conversia audio stereo la cel mai înalt nivel de calitate:

`opusenc --bitrate {{512}} {{path/to/input.wav}} {{path/to/output}}.opus`

- Conversia sunetului surround 5.1 audio la cel mai înalt nivel de calitate:

`opusenc --bitrate {{1536}} {{path/to/input.flac}} {{path/to/output}}.opus`

- Conversia audio de vorbire la cel mai scăzut nivel de calitate:

`opusenc {{path/to/input.wav}} --downmix-mono --bitrate {{6}} {{path/to/out}}.opus`
