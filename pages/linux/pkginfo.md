# pkginfo

> Query the package database on a CRUX system.
> More information: <https://crux.nu/Main/Handbook3-6#ntoc19>.

- List installed packages and their versions:

`pkginfo -i`

- List files owned by a package:

`pkginfo -l {{package}}`

- List the owner(s) of files matching a pattern:

`pkginfo -o {{pattern}}`

- Print the footprint of a file:

`pkginfo -f {{path/to/file}}`
