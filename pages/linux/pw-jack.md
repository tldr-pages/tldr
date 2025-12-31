# pw-jack

> Run a JACK application with PipeWire.
> More information: <https://docs.pipewire.org/page_man_pw-jack_1.html>.

- Run a command with its arguments, using PipeWire:

`pw-jack {{command}} {{argument1 argument2 ...}}`

- Run a command in verbose mode:

`pw-jack -v {{command}}`

- Connect to a specific remote PipeWire instance:

`pw-jack -r {{remote_instance_name}} {{command}}`

- Display help:

`pw-jack -h`
