# aurman

> An Arch Linux utility to build and install packages from the Arch User Repository.
> See also: `pacman`.
> More information: <https://github.com/polygamma/aurman#syntax>.

- Synchronize and update all packages:

`aurman {{[-S|--sync]}} {{[-y|--refresh]}} {{[-u|--sysupgrade]}}`

- Synchronize and update all packages without show changes of `PKGBUILD` files:

`aurman {{[-S|--sync]}} {{[-y|--refresh]}} {{[-u|--sysupgrade]}} --noedit`

- Install a new package:

`aurman {{[-S|--sync]}} {{package}}`

- Install a new package without show changes of `PKGBUILD` files:

`aurman {{[-S|--sync]}} --noedit {{package}}`

- Install a new package without prompting:

`aurman {{[-S|--sync]}} --noedit --noconfirm {{package}}`

- Search the package database for a keyword from the official repositories and AUR:

`aurman {{[-S|--sync]}} {{[-s|--search]}} {{keyword}}`

- Remove a package and its dependencies:

`aurman --remove --recursive --nosave {{package}}`

- Clear the package cache (use two `--clean` flags to clean all packages):

`aurman {{[-S|--sync]}} {{[-c|--clean]}}`
