# pw-mididump

> Dump MIDI messages to `stdout`.
> More information: <https://docs.pipewire.org/page_man_pw-mididump_1.html>.

- Listen for and dump all incoming MIDI events:

`pw-mididump`

- Dump MIDI events from a specific file:

`pw-mididump {{path/to/file.mid}}`

- Connect to a specific remote PipeWire instance:

`pw-mididump {{[-r|--remote]}} {{remote_instance_name}}`

- Display help:

`pw-mididump {{[-h|--help]}}`
