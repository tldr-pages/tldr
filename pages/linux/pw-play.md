# pw-play

> Play audio files through PipeWire.
> Shorthand for `pw-cat --playback`.
> See also: `play`.
> More information: <https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>.

- Play a WAV sound file over the default target:

`pw-play {{path/to/file.wav}}`

- Play a WAV sound file at a different volume level:

`pw-play --volume={{0.1}} {{path/to/file.wav}}`
