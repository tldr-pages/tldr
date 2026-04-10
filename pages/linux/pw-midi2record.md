# pw-midi2record

> Record MIDI 2.0 clips through PipeWire.
> Note: This command is an alias of `pw-cat --record --midi-clip`.
> See also: `pw-cat`, `pw-midi2play`, `pw-midirecord`.
> More information: <https://docs.pipewire.org/page_man_pw-cat_1.html>.

- Record a MIDI 2.0 clip file from the default source:

`pw-midi2record {{path/to/file.mid}}`

- Record a MIDI clip, forcing the MIDI format to use (defaults to `ump`):

`pw-midi2record {{[-M|--force-midi]}} {{midi|ump}} {{path/to/file.mid}}`

- Display help:

`pw-midi2record {{[-h|--help]}}`
