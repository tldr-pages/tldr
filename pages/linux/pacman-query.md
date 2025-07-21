# pacman --query

> Arch Linux package manager utility.
> See also: `pacman`.
> More information: <https://manned.org/pacman.8>.

- Query the local package database and list installed packages and versions:

`pacman {{[-Q|--query]}}`

- List only packages and versions that were explicitly installed:

`pacman {{[-Qe|--query --explicit]}}`

- Find which package owns a file:

`pacman {{[-Qo|--query --owns]}} {{filename}}`

- Display information about an installed package:

`pacman {{[-Qi|--query --info]}} {{package}}`

- Display the list of files owned by a specific package:

`pacman {{[-Ql|--query --list]}} {{package}}`

- List orphan packages (installed as dependencies but unrequired by any package and print in quiet mode (only package name is displayed)):

`pacman {{[-Qdtq|--query --deps --unrequired --quiet]}}`

- List installed packages foreign to the repository database:

`pacman {{[-Qm|--query --foreign]}}`

- List packages that can be upgraded:

`pacman {{[-Qu|--query --upgrades]}}`
