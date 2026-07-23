# free

> Display amount of free and used memory in the system.
> More information: <https://manned.org/free>.

- Display system memory in KiB:

`free`

- Display memory in bytes/KiB/MiB/GiB:

`free -{{b|k|m|g}}`

- Display memory in the most appropriate human-readable units (KiB/MiB/GiB etc):

`free {{[-h|--human]}}`

- Display memory in the most appropriate human-readable unit that is a power of 1000 (kB/MB/GB etc):

`free {{-h|--human}} --si`

- Refresh the output every 2 seconds:

`free {{[-s|--seconds]}} 2`
