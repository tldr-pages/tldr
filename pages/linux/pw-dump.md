# pw-dump

> Dump PipeWire's current state as JSON, including the information on nodes, devices, modules, ports, and other objects.
> See also: `pw-mon`.
> More information: <https://docs.pipewire.org/page_man_pw-dump_1.html>.

- Print a JSON representation of the default PipeWire instance's current state:

`pw-dump`

- Print a JSON representation of an object:

`pw-dump {{object_id}}`

- Dump the current state monitoring changes, printing it again:

`pw-dump {{[-m|--monitor]}}`

- Dump the current state of a remote instance to a file:

`pw-dump {{[-r|--remote]}} {{remote_name}} > {{path/to/dump_file.json}}`

- Set a color configuration:

`pw-dump {{[-C|--color]}} {{never|always|auto}}`

- Display help:

`pw-dump {{[-h|--help]}}`
