# pacman --remove

> Arch Linux package manager utility.
> See also: `pacman`.
> More information: <https://man.archlinux.org/man/pacman.8>.

- Remove a package and its dependencies:

`sudo pacman --remove --recursive {{package}}`

- Remove a package and both its dependencies and configuration files:

`sudo pacman --remove --recursive --nosave {{package}}`

- Remove a package without prompting:

`sudo pacman --remove --noconfirm {{package}}`

- Remove orphan packages (installed as dependencies but not required by any package):

`sudo pacman --remove --recursive --nosave $(pacman --query --unrequired --deps --quiet)`

- Remove a package and all packages that depend on it:

`sudo pacman --remove --cascade {{package}}`

- List packages that would be affected (does not remove any packages):

`pacman --remove --print {{package}}`

- Display help for this subcommand:

`pacman --remove --help`
