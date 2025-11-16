# apt

> Package manager for Debian-based distributions.
> Intended as a user-friendly alternative to `apt-get` for interactive use.
> For equivalent commands in other package managers, see <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> More information: <https://wiki.debian.org/apt>.

- Update the list of available packages and versions (recommended to run before install or upgrade):

`sudo apt update`

- Search packages by name or description:

`apt search {{package}}`

- Search packages by name only (supports wildcards like `*`):

`apt list {{package}}`

- Show detailed information about a package:

`apt show {{package}}`

- Install a package, or update it to the latest version:

`sudo apt install {{package}}`

- Remove a package (use `purge` instead to also remove configuration files):

`sudo apt remove {{package}}`

- Upgrade all installed packages to their latest versions:

`sudo apt upgrade`

- List installed packages only:

`apt list --installed`
