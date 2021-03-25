# aurman

> An Arch Linux utility to build and install packages from the Arch User Repository.
> See also `pacman`.
> More information: <https://github.com/polygamma/aurman>.

- Synchronize and update all packages:

`aurman --sync --refresh --sysupgrade`

- Synchronize and update all packages without show changes of `PKGBUILD` files:

`aurman --sync --refresh --sysupgrade --noedit`

- Install a new package:

`aurman --sync {{package_name}}`

- Install a new package without show changes of `PKGBUILD` files:

`aurman --sync --noedit {{package_name}}`

- Install a new package without prompting:

`aurman --sync --noedit --noconfirm {{package_name}}`

- Search the package database for a keyword from the official repositories and AUR:

`aurman --sync --search {{keyword}}`

- Remove a package and its dependencies:

`aurman --remove --recursive --nosave {{package_name}}`

- Clear the package cache (use two `--clean` flags to clean all packages):

`aurman --sync --clean`
