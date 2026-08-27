# clinfo

> Display information about all available OpenCL platforms and devices.
> More information: <https://github.com/Oblomov/clinfo>.

- Display all available information about all OpenCL platforms and devices:

`clinfo`

- List platform and device names only, without properties:

`clinfo {{[-l|--list]}}`

- Display properties of a specific device of a specific platform (indices as shown by `clinfo --list`):

`clinfo {{[-d|--device]}} {{platform_index}}:{{device_index}}`

- Display only properties whose symbolic name contains a specific substring:

`clinfo --prop {{property_name}}`

- Try to display all properties, even those not officially supported:

`clinfo {{[-a|--all-props]}}`

- Produce machine-friendly raw output:

`clinfo --raw`

- Produce output in JSON format (experimental):

`clinfo --json`

- Display version:

`clinfo {{[-v|--version]}}`
