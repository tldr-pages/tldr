# apt

> Package management utility for Debian based distributions.
> Recommended replacement for apt-get when used interactively in Ubuntu versions 16.04 and later.

- Update the list of available packages and versions (it's recommended to run this before other `apt` commands):

`sudo apt update`

- Search for a given package:

`apt search {{package}}`

- Show information for a package:

`apt show {{package}}`

- Install a package, or update it to the latest available version:

`sudo apt install {{package}}`

- Remove a package (using `purge` instead also removes its configuration files):

`sudo apt remove {{package}}`

- Upgrade all installed packages to their newest available versions:

`sudo apt upgrade`

- List all packages:

`apt list`

- List installed packages:

`apt list --installed`
