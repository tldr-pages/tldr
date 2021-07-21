# nettop

> Display dynamic real-time information about the network.
More information: <N/A>.
- Monitor TCP and UDP sockets from all interfaces:

`nettop`

- Monitor TCP sockets from Loopback interfaces:

`nettop -m {{tcp}} -t {{loopback}}`

- Monitor a specific process:

`nettop -p {{process_id|process_name}}`

- Display summary only for per-process:

`nettop -P`

- Monitor in logging mode and display 10 samples:

`nettop -l {{10}}`

- Monitor in delta mode, updating every 5 seconds:

`nettop -d -s {{5}}`

- While running nettop, list interactive commands:

`h`

- Display help:

`nettop -h`
