# opusenc

> Convert WAV or FLAC audio to Opus.
> More information: <https://opus-codec.org/docs/opus-tools/opusenc.html.

- Convert WAV to Opus using default options:

`opusenc {{input.wav}} {{output}}.opus`

- Convert stereo audio at the highest quality level:

`opusenc --bitrate 512 {{input.wav|input.flac}} {{output}}.opus`

- Convert 5.1 surround sound audio at the highest quality level:

`opusenc --bitrate 1536 {{input.flac}} {{output}}.opus`

- Convert speech audio at the lowest quality level:

`opusenc {{input.wav}} --downmix-mono --bitrate 6 {{out}}.opus`
