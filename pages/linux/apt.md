# apt

> Package management utility for Debian based distributions.
> Recommended replacement for `apt-get` when used interactively in Ubuntu versions 16.04 and later.
> For equivalent commands in other package managers, see <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> More information: <https://manned.org/apt.8>.

- Update the list of available packages and versions (it's recommended to run this before other `apt` commands):

`sudo apt update`

- Search for a given package (use `apt search --name-only package` to search within package name only):

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

`apt list {{[-i|--installed]}}`
