# pkginfo

> Query the package database on a CRUX system.
> More information: <https://crux.nu/Main/Handbook3-6#ntoc19>.

- List installed packages and their versions:

`pkginfo {{[-i|--installed]}}`

- List files owned by a package:

`pkginfo {{[-l|--list]}} {{package}}`

- List the owner(s) of files matching a pattern:

`pkginfo {{[-o|--owner]}} {{pattern}}`

- Print the footprint of a file:

`pkginfo -f {{path/to/file}}`
