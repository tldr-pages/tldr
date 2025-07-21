# pacman --database

> Operate on the Arch Linux package database.
> Modify certain attributes of the installed packages.
> See also: `pacman`.
> More information: <https://manned.org/pacman.8>.

- Mark a package as implicitly installed:

`sudo pacman {{[-D|--database]}} --asdeps {{package}}`

- Mark a package as explicitly installed:

`sudo pacman {{[-D|--database]}} --asexplicit {{package}}`

- Check that all the package dependencies are installed:

`pacman {{[-Dk|--database --check]}}`

- Check the sync database to ensure all specified dependencies of downloadable packages are available:

`pacman {{[-Dkk|--database --check --check]}}`

- Check and display in quiet mode (only error messages are displayed):

`pacman {{[-Dkq|--database --check --quiet]}}`

- Display help:

`pacman {{[-Dh|--database --help]}}`
