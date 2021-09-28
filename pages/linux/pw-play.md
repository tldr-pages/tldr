# pw-play

> Shorthand tool for pw-cat --playback.
> More information: <https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>.

- List all available playback targets:

`pw-play --list-targets`

- Play a wav sound file over the default target:

`pw-play {{path/to/file.wav}}`

- Play a wav sound file at a different volume level:

`pw-play --volume={{0.1}} {{path/to/file.wav}}`
