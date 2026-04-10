# pw-midi2play

> Play MIDI 2.0 clips through PipeWire.
> Note: This command is an alias of `pw-cat --playback --midi-clip`.
> See also: `pw-cat`, `pw-midi2record`, `pw-midiplay`.
> More information: <https://docs.pipewire.org/page_man_pw-cat_1.html>.

- Play a MIDI 2.0 clip file over the default target:

`pw-midi2play {{path/to/file.mid}}`

- Play a MIDI clip, forcing the MIDI format to use (defaults to `ump`):

`pw-midi2play {{[-M|--force-midi]}} {{midi|ump}} {{path/to/file.mid}}`

- Display help:

`pw-midi2play {{[-h|--help]}}`
