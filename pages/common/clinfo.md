# clinfo

> Display information about OpenCL platforms and devices.
> More information: <https://github.com/Oblomov/clinfo>.

- Display full OpenCL system information:

`clinfo`

- List all available platforms and devices by name:

`clinfo --list`

- Display detailed information for a specific platform and device:

`clinfo --device {{platform_index}}:{{device_index}}`

- Display raw property values without human-readable formatting:

`clinfo --raw`

- Output information in JSON format:

`clinfo --json`
