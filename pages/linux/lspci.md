# lspci

> List all PCI devices.

- Show a brief list of devices:

`lspci`

- Display additional info:

`lspci -v`

- Display drivers and modules handling each device:

`lspci -k`

- Show a specific device: 

`lspci -s {{bus:device.func}}`

- Dump info in readable form:

`lspci -vm`
