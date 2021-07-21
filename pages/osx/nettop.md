# nettop

> Display dynamic real-time information about the network.

- Start nettop monitoring TCP and UDP sockets from all interfaces:

`nettop`

- Start nettop monitoring TCP sockets from Loopback interfaces:

`nettop -m tcp -t loopback`

- Start nettop monitoring specific process:

`nettop -p {{process_id|process_name}}`

- Start nettop displaying summary only for per-process:

`nettop -P`

- Start nettop in logging mode and display 10 samples:

`nettop -l {{10}}`

- Start nettop in delta mode, updating every 5 seconds:

`nettop -d -s {{5}}`

- See interactive commands while running nettop:

`h`

- Display help message:

`nettop -h`
