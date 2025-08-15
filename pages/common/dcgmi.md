# dcgmi

> Manage and monitor NVIDIA Data Center GPUs.
> More information: <https://developer.nvidia.com/dcgm>.

- Display information on all available GPUs and processes using them:

`dcgmi discovery {{[-l|--list]}}`

- List created groups:

`dcgmi group {{[-l|--list]}}`

- Display current usage statistics for device 0:

`dcgmi dmon {{[-e|--field-id]}}{{1001,1002,1003,1004,1005}}`

- Display help:

`dcgmi {{[-h|--help]}}`

- Display help for a subcommand:

`dcgmi {{subcommand}} {{[-h|--help]}}`
