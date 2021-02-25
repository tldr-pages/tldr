# pacman --upgrade

> Arch Linux package manager utility.
> More information: <https://man.archlinux.org/man/pacman.8>.

- Display help:

`pacman --upgrade --help`

- Install one or more packages from files:

`sudo pacman --upgrade {{path/to/package1}} {{path/to/package2}}`

- Install a package without prompting:

`sudo pacman --upgrade --noconfirm {{path/to/package}}`

- Overwrite conflicting files during a package installation:

`sudo pacman --upgrade --overwrite {{path/to/file}} {{path/to/package}}`

- Install a package, skipping the dependency version checks:

`sudo pacman --upgrade --nodeps {{path/to/package}}`

- List packages that would be affected (does not install any packages):

`pacman --query --print {{path/to/package}}`
