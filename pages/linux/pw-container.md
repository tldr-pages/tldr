# pw-container

> Run a program in a new security context.
> More information: <https://docs.pipewire.org/page_man_pw-container_1.html>.

- Create a new security context and print its socket address to `stdout`:

`pw-container`

- Run a specific program within a new security context:

`pw-container {{command}} {{argument1 argument2 ...}}`

- Run a program, connecting to a specific remote PipeWire instance:

`pw-container {{[-r|--remote]}} {{remote_instance_name}} {{command}}`

- Run a program in a new context with specific properties using a JSON object:

`pw-container {{[-P|--properties]}} '{{{"key": "value"}}}' {{command}}`

- Display help:

`pw-container {{[-h|--help]}}`
