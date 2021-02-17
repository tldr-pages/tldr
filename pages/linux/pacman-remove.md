# pacman --remove

> Arch Linux package manager utility.
> More information: <https://man.archlinux.org/man/pacman.8>.

- Display help for this subcommand:

`pacman --remove --help`

- Remove a package and its dependencies:

`pacman --remove --recursive {{package_name}}`

- Remove a package and its dependencies and configuration files:

`pacman --remove --recursive --nosave {{package_name}}`

- Remove a package without prompting:

`pacman --remove --noconfirm {{filename}}`

- Remove orphan packages (installed as dependencies but not required by any package):

`pacman --remove --recursive --nosave $(pacman --query --unrequired --deps --quiet)`

- Remove a package and all packages that depend on them:

`pacman --remove --cascade {{package_name}}`

- List the affect packages without remove them:

`pacman --remove --print {{package_name}}`
