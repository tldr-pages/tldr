# opusenc

> WAV vagy FLAC audió konvertálása Opusba. További információ: <https://opus-codec.org/docs/opus-tools/opusenc.html>.

- WAV konvertálása Opusba az alapértelmezett beállításokkal:

`opusenc {{path/to/input.wav}} {{path/to/output}}.opus`

- Sztereó hang konvertálása a legmagasabb minőségi szinten:

`opusenc --bitrate {{512}} {{path/to/input.wav}} {{path/to/output}}.opus`

- 5.1 surround hangzású hang konvertálása a legmagasabb minőségi szinten:

`opusenc --bitrate {{1536}} {{path/to/input.flac}} {{path/to/output}}.opus`

- Beszédhang konvertálása a legalacsonyabb minőségi szinten:

`opusenc {{path/to/input.wav}} --downmix-mono --bitrate {{6}} {{path/to/out}}.opus`
