# repo-add

> Package database maintenance utility which enables installation of said package via Pacman.
> More information: <https://manned.org/repo-add>.

- Create an empty repository:

`repo-add {{path/to/database.db.tar.gz}}`

- Add all package binaries in the current directory and remove the old database file:

`repo-add {{[-R|--remove]}} {{path/to/database.db.tar.gz}} {{*.pkg.tar.zst}}`

- Add all package binaries in the current directory in silent mode except for warning and error messages:

`repo-add {{[-q|--quiet]}} {{path/to/database.db.tar.gz}} {{*.pkg.tar.zst}}`

- Add all package binaries in the current directory without showing color:

`repo-add --nocolor {{path/to/database.db.tar.gz}} {{*.pkg.tar.zst}}`
