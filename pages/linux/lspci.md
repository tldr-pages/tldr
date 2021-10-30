# lspci

> List all PCI devices.
> More information: <https://manned.org/lspci>.

- Show a brief list of devices:

`lspci`

- Display additional info:

`lspci -v`

- Display drivers and modules handling each device:

`lspci -k`

- Show a specific device:

`lspci -s {{00:18.3}}`

- Dump info in a readable form:

`lspci -vm`
