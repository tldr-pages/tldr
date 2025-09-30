# pacman --database

> Operate on the Arch Linux package database.
> Modify certain attributes of the installed packages.
> See also: `pacman`.
> More information: <https://manned.org/pacman.8>.

- Mark a package as implicitly installed:

`sudo pacman -D --asdeps {{package}}`

- Mark a package as explicitly installed:

`sudo pacman -D --asexplicit {{package}}`

- Chec[k] that all the package dependencies are installed:

`pacman -Dk`

- Chec[k] the sync [D]atabase to ensure all specified dependencies of downloadable packages are available:

`pacman -Dkk`

- Chec[k] and display in [q]uiet mode (only error messages are displayed):

`pacman -Dkq`

- Display [h]elp:

`pacman -Dh`
