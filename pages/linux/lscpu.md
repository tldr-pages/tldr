# lscpu

> Display information about the CPU architecture.
> More information: <https://manned.org/lscpu>.

- Display information about all CPUs:

`lscpu`

- Display information in a table:

`lscpu {{[-e|--extended]}}`

- Display only information about online CPUs in a table:

`lscpu {{[-e|--extended]}} {{[-b|--online]}}`

- Display only information about offline CPUs in a table:

`lscpu {{[-e|--extended]}} {{[-c|--offline]}}`

- Display details about CPU caches:

`lscpu {{[-C|--caches]}}`

- Display information in JSON format:

`lscpu {{[-J|--json]}}`
