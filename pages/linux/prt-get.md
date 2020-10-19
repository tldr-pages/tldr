# prt-get

> The CRUX package manager.

- Install a package:

`prt-get install {{package_name}}`

- Install a package with dependency handling:

`prt-get depinst {{package_name}}`

- Update a package manually:

`prt-get upgrade {{package_name}}`

- Remove a package:

`prt-get remove {{package_name}}`

- Upgrade the system from the local ports tree:

`prt-get sysup`

- Search the ports tree:

`prt-get search {{package_name}}`

- Search for a file in a package:

`prt-get fsearch {{file}}`
