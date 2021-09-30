# repo-add

> Package database maintenance utility which enables installation via pacman.

- Add all package binaries in the current directory and remove the old database file:

`repo-add --remove {{your_database_name.db.tar.gz *.pkg.tar.zst}}`

- Add all package binaries in the current directory in silent mode except for warning and error messages:

`repo-add --quiet {{your_database_name.db.tar.gz *.pkg.tar.zst}}`

- Remove color from output:

`repo-add --nocolor {{your_database_name.db.tar.gz *.pkg.tar.zst}}`
