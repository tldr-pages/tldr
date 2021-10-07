# repo-add

> Package database maintenance utility which enables installation of said package via Pacman.
> More information: <https://man.archlinux.org/man/repo-add>.

- Add all package binaries in the current directory and remove the old database file:

`repo-add --remove {{path/to/database.db.tar.gz}} {{*.pkg.tar.zst}}`

- Add all package binaries in the current directory in silent mode except for warning and error messages:

`repo-add --quiet {{path/to/database.db.tar.gz}} {{*.pkg.tar.zst}}`

- Add all package binaries in the current directory without showing color:

`repo-add --nocolor {{path/to/database.db.tar.gz}} {{*.pkg.tar.zst}}`
