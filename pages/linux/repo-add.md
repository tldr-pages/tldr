# repo-add

> Package database maintenance utility which enables installation of said package via Pacman.
> See also: `repo-remove`.
> More information: <https://manned.org/repo-add>.

- Create an empty repository:

`repo-add {{path/to/database.db.tar.gz}}`

- Add packages to the repository:

`repo-add {{path/to/database.db.tar.gz}} {{package1.pkg.tar.zst package2.pkg.tar.zst ...}}`

- Add all package binaries in the current directory and remove any outdated package files:

`repo-add {{[-R|--remove]}} {{path/to/database.db.tar.gz}} {{*.pkg.tar.zst}}`

- Add all package binaries in the current directory in silent mode except for warning and error messages:

`repo-add {{[-q|--quiet]}} {{path/to/database.db.tar.gz}} {{*.pkg.tar.zst}}`

- Add all package binaries in the current directory without showing color:

`repo-add --nocolor {{path/to/database.db.tar.gz}} {{*.pkg.tar.zst}}`
