# clinfo

> Show OpenCL platforms and devices.
> More information: <https://manned.org/man/clinfo>.

- Display information about all OpenCL platforms and devices:

`clinfo`

- List platforms and devices by name:

`clinfo {{[-l|--list]}}`

- Display information for a specific device:

`clinfo {{[-d|--device]}} {{platform_index}}:{{device_index}}`

- Display machine-friendly output:

`clinfo --raw`

- Include offline devices:

`clinfo --offline`

- Try to retrieve all properties, including unofficial ones:

`clinfo {{[-a|--all-props]}}`

- Display only properties matching the given property name:

`clinfo --prop {{property_name}}`
