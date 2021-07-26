# synopkg

> Package management utility for Synology DiskStation Manager.
> More information: <https://www.synology.com/dsm>.

- List the names of installed packages:

`synopkg list --name`

- List packages which depend on a specific package:

`synopkg list --depend-on {{package}}`

- Start/Stop a package:

`sudo synopkg {{start|stop}} {{package}}`

- Print the status of a package:

`synopkg status {{package}}`

- Uninstall a package:

`sudo synopkg uninstall {{package}}`

- Check if a package is updatable:

`synopkg checkupdate {{package}}`

- Upgrade all packages to the latest version:

`sudo synopkg upgradeall`

- Install a package from file:

`sudo synopkg install {{path/to/package.spk}}`
