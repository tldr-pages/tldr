# pacman

> Arch Linux package manager utility

- synchronize and update all packages

`pacman -Syyu`

- install a new package

`pacman -S package-name`

- remove a package and its dependencies

`pacman -Rs package-name`

- search the package database for a keyword

`pacman -Ss icon theme`

- list installed packages and versions

`pacman -Q`

- list only the explicitly installed packages and versions

`pacman -Qe`

- find which package owns a certain file

`pacman -Qo filename`

- empty package cache to free up space

`pacman -Scc`
