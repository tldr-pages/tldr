# pw-link

> Manage links between ports in PipeWire.
> More information: <https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Virtual-Devices>.

- List all audio output and input ports with their IDs:

`pw-link {{[-oiI|--output --input --ids]}}`

- Create a link between an output and an input port:

`pw-link {{output_port_name}} {{input_port_name}}`

- Disconnect two ports:

`pw-link {{[-d|--disconnect]}} {{output_port_name}} {{input_port_name}}`

- List all links with their IDs:

`pw-link {{[-lI|--links --ids]}}`

- Display help:

`pw-link {{[-h|--help]}}`
