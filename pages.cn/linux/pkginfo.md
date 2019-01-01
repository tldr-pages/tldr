# pkginfo

> Query the package database on a CRUX system.

- List installed packages and their versions:

`pkginfo -i`

- List files owned by a package:

`pkginfo -l {{package_name}}`

- List the owner(s) of files matching a pattern:

`pkginfo -o {{pattern}}`

- Print the footprint of a file:

`pkginfo -f {{file}}`
