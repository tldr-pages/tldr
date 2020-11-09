# opusenc

> Converte audio WAV o FLAC in Opus.
> Maggiori informazioni: <https://opus-codec.org/docs/opus-tools/opusenc.html>.

- Converte un file WAV in un file Opus usando le opzioni predefinite:

`opusenc {{percorso/al/file_originale.wav}} {{percorso/al/file_convertito}}.opus`

- Converte un audio stereo alla massima qualità possibile:

`opusenc --bitrate {{512}} {{percorso/al/file_originale.wav}} {{percorso/al/file_convertito}}.opus`

- Converte un audio con canali surround 5.1 alla massima qualità possibile:

`opusenc --bitrate {{1536}} {{percorso/al/file_originale.flac}} {{percorso/al/file_convertito}}.opus`

- Converte l'audio di una voce alla minima qualità possibile:

`opusenc {{percorso/al/file_originale.wav}} --downmix-mono --bitrate {{6}} {{percorso/al/file_convertito}}.opus`
