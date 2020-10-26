# opusenc

> Converte audio WAV o FLAC in Opus.
> Maggiori informazioni: <https://opus-codec.org/docs/opus-tools/opusenc.html>.

- Converte un file WAV in un file Opus usando le opzioni predefinite:

`opusenc {{percorso/all/input.wav}} {{percorso/all/output}}.opus`

- Converte un audio stereo alla massima qualità possibile:

`opusenc --bitrate {{512}} {{percorso/all/input.wav}} {{percorso/all/output}}.opus`

- Converte un audio con canali surround 5.1 alla massima qualità possibile:

`opusenc --bitrate {{1536}} {{percorso/all/input.flac}} {{percorso/all/output}}.opus`

- Converte l'audio di una voce alla minima qualità possibile:

`opusenc {{path/to/input.wav}} --downmix-mono --bitrate {{6}} {{path/to/out}}.opus`
