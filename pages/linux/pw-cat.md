# pw-cat

> Play and record audio files through pipewire.
> More information: <https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>.

- Play a WAV file over the default target:

`pw-cat --playback {{path/to/file.wav}}`

- Play a WAV file with a specified resampler quality (4 by default):

`pw-cat --quality {{0..15}} --playback {{path/to/file.wav}}`

- Record a sample recording at a volume level of 125%:

`pw-cat --record --volume {{1.25}} {{path/to/file.wav}}`

- Record a sample recording using a different sample rate:

`pw-cat --record --rate {{6000}} {{path/to/file.wav}}`
