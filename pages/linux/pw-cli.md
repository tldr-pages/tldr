# pw-cli

> Manage a PipeWire instance's modules, objects, nodes, devices, links and much more.
> See also: `wpctl`.
> More information: <https://docs.pipewire.org/page_man_pw-cli_1.html>.

- Print information of all object of a specific type:

`pw-cli {{[ls|list-objects]}} {{Node|Link|Port|Client|Device|Metadata|Factory|Module|Profiler|SecurityContext|Core}}`

- Print information about an object with a specific ID:

`pw-cli {{[i|info]}} {{4}}`

- Print all objects' information:

`pw-cli {{[i|info]}} all`

- Monitor for object changes:

`pw-cli {{[-m|--monitor]}}`

- Display help:

`pw-cli {{[h|help]}}`
