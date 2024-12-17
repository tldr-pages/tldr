# pacman --database

> Operate on the Arch Linux package database.
> Modify certain attributes of the installed packages.
> See also: `pacman`.
> More information: <https://manned.org/pacman.8>.

- Mark a package as implicitly installed:

`sudo pacman --D --asdeps {{package}}`

- Mark a package as explicitly installed:

`sudo pacman --D --asexplicit {{package}}`

- Check that all the package dependencies are installed:

`pacman --D --check`

- Check the repositories to ensure all specified dependencies are available:

`pacman --D --check --check`

- Display only error messages:

`pacman --D --check --quiet`

- Display help:

`pacman --D --help`
