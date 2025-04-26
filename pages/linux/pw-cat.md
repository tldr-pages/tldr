# pw-cat

> Play and record audio files through PipeWire.
> More information: <https://docs.pipewire.org/page_man_pw-cat_1.html>.

- Play a WAV file over the default target:

`pw-cat {{[-p|--playback]}} {{path/to/file.wav}}`

- Play a WAV file with a specified resampler quality (4 by default):

`pw-cat {{[-q|--quality]}} {{0..15}} {{[-p|--playback]}} {{path/to/file.wav}}`

- Record a sample recording at a volume level of 125%:

`pw-cat {{[-r|--record]}} --volume {{1.25}} {{path/to/file.wav}}`

- Record a sample recording using a different sample rate:

`pw-cat {{[-r|--record]}} --rate {{6000}} {{path/to/file.wav}}`

- Display help:

`pw-cat {{[-h|--help]}}`
