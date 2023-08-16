# pacman --query

> Arch Linux package manager utility.
> See also: `pacman`.
> More information: <https://man.archlinux.org/man/pacman.8>.

- List installed packages and versions:

`pacman --query`

- List only packages and versions that were explicitly installed:

`pacman --query --explicit`

- Find which package owns a file:

`pacman --query --owns {{filename}}`

- Display information about an installed package:

`pacman --query --info {{package_name}}`

- List files owned by a package:

`pacman --query --list {{package_name}}`

- List orphan packages (installed as dependencies but not required by any package):

`pacman --query --unrequired --deps --quiet`

- List installed packages not found in the repositories:

`pacman --query --foreign`

- List outdated packages:

`pacman --query --upgrades`
