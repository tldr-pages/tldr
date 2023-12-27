# pw-dump

> Dump PipeWire's current state as JSON, including the information on nodes, devices, modules, ports, and other objects.
> See also: `pw-mon`.
> More information: <https://docs.pipewire.org/page_man_pw-dump_1.html>.

- Print a JSON representation of the default PipeWire instance's current state:

`pw-dump`

- Dump the current state [m]onitoring changes, printing it again:

`pw-dump --monitor`

- Dump the current state of a [r]emote instance to a file:

`pw-dump --remote {{remote_name}} > {{path/to/dump_file.json}}`

- Set a [C]olor configuration:

`pw-dump --color {{never|always|auto}}`

- Display help:

`pw-dump --help`
