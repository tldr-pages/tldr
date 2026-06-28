# wineserver

> Manage the Wine server, the daemon that backs each Wine prefix.
> More information: <https://manned.org/wineserver>.

- [k]ill the current Wine server, terminating all of its Wine processes:

`wineserver {{[-k|--kill]}}`

- [w]ait until the current Wine server has finished:

`wineserver {{[-w|--wait]}}`

- Keep the server [p]ersistent so it does not exit when the last process closes:

`wineserver {{[-p|--persistent]}}`

- Display version:

`wineserver {{[-v|--version]}}`

- Display help:

`wineserver {{[-h|--help]}}`
