# pacman --deptest

> Check each dependency specified and return a list of dependencies that are not currently satisfied on the system.
> See also: `pacman`.
> More information: <https://man.archlinux.org/man/pacman.8>.

- Print the package names of the dependencies that aren't installed:

`pacman --deptest {{package1 package2 ...}}`

- Check if the installed package satisfies the given minimum version:

`pacman --deptest "{{bash>=5}}"`

- Check if a later version of a package is installed:

`pacman --deptest "{{bash>5}}"`

- Display help:

`pacman --deptest --help`
