# pacman

> Arch Linux package manager utility.
> More information: <https://man.archlinux.org/man/pacman.8>.

- Synchronize and update all packages:

`pacman -Syu`

- Install a new package:

`pacman -S {{package_name}}`

- Remove a package and its dependencies:

`pacman -Rs {{package_name}}`

- Search the package database for a regular expression or keyword:

`pacman -Ss "{{search_pattern}}"`

- List installed packages and versions:

`pacman -Q`

- List only the explicitly installed packages and versions:

`pacman -Qe`

- Find which package owns a certain file:

`pacman -Qo {{filename}}`

- Empty package cache to free up space:

`pacman -Scc`
