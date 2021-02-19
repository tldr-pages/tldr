# pacman --remove

> Arch Linux package manager utility.
> More information: <https://man.archlinux.org/man/pacman.8>.

- Display help for this subcommand:

`pacman --remove --help`

- Remove a package and its dependencies:

`sudo pacman --remove --recursive {{package_name}}`

- Remove a package and both its dependencies and configuration files:

`sudo pacman --remove --recursive --nosave {{package_name}}`

- Remove a package without prompting:

`sudo pacman --remove --noconfirm {{package_name}}`

- Remove orphan packages (installed as dependencies but not required by any package):

`sudo pacman --remove --recursive --nosave $(pacman --query --unrequired --deps --quiet)`

- Remove a package and all packages that depend on it:

`sudo pacman --remove --cascade {{package_name}}`

- List packages that would be affected (does not remove any packages):

`pacman --remove --print {{package_name}}`
