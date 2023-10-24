# pw-cat

> Play and record audio files through pipewire.
> More information: <https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>.

- Play a WAV file over the default target:

`pw-cat --playback {{path/to/file.wav}}`

- Record a sample recording at a different volume level:

`pw-cat --record --volume={{0.1}} {{path/to/file.wav}}`

- Record a sample recording using a different sample rate:

`pw-cat --record --rate={{6000}} {{path/to/file.wav}}`
