# paru

> An AUR helper and pacman wrapper.
> See also: `pacman`, `yay`.
> More information: <https://github.com/Morganamilo/paru#examples>.

- Interactively search for and install a package:

`paru {{package_name_or_search_term}}`

- Synchronize and update all packages:

`paru`

- Upgrade AUR packages:

`paru -Sua`

- Remove an installed package, it's configuration files, and dependencies:

`paru -Rns {{package}}`

- Get information about a package:

`paru -Si {{package}}`

- Download `PKGBUILD` and other package source files from the AUR or ABS:

`paru --getpkgbuild {{package}}`

- Display the `PKGBUILD` file of a package:

`paru --getpkgbuild --print {{package}}`
