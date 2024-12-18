# pacman --database

> Operate on the Arch Linux package database.
> Modify certain attributes of the installed packages.
> See also: `pacman`.
> More information: <https://manned.org/pacman.8>.

- Mark a package as implicitly installed:

`sudo pacman -D --asdeps {{package}}`

- Mark a package as explicitly installed:

`sudo pacman -D --asexplicit {{package}}`

- Check ([k]) that all the package dependencies are installed:

`pacman -Dk`

- Double check ([kk]) the sync database to ensure all specified dependencies are available:

`pacman -Dkk`

- Check ([k]) and display in quiet ([q]) mode (no error message displayed): 

`pacman -Dkq`

- Display help:

`pacman -D --help`
