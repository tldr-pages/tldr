# pw-link

> Manage links between ports in PipeWire.
> More information: <https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Virtual-Devices>.

- List all audio output and input ports:

`pw-link --output --input'`

- Create a link between an output and an input port:

`pw-link {{output_port_name}} {{input_port_name}}`

- Disconnect two ports:

`pw-link --disconnect {{output_port_name}} {{input_port_name}}`

- Display help:

`pw-link -h`
