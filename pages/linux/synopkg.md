# synopkg

> Package management utility for Synology DiskStation Manager.
> More information: <https://www.synology.com/dsm>.

- List installed packages without description:

`synopkg list --name`

- List packages depend on a specific package:

`synopkg list --depend-on {{package}}`

- Start/Stop a package:

`sudo synopkg {{start|stop}} {{package}}`

- Print the status of a package:

`synopkg status {{package}}`

- Uninstall a package:

`sudo synopkg uninstall {{package}}`

- Check if a package is updateable:

`synopkg checkupdate {{package}}`

- Upgrade all packages to latest version:

`sudo synopkg upgradeall`

- Install a package from file:

`sudo synopkg install {{path/to/package.spk}}`
