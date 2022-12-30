# pacman --database

> Operate on the Arch Linux package database.
> Modify certain attributes of the installed packages.
> More information: <https://man.archlinux.org/man/pacman.8>.

- Mark a package as implicitly installed:

`sudo pacman --database --asdeps {{package_name}}`

- Mark a package as explicitly installed:

`sudo pacman --database --asexplicit {{package_name}}`

- Check that all the package dependencies are installed:

`pacman --database --check`

- Check the repositories to ensure all specified dependencies are available:

`pacman --database --check --check`

- Display only error messages:

`pacman --database --check --quiet`

- Display help:

`pacman --database --help`
