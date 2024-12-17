# pacman --query

> Arch Linux package manager utility.
> See also: `pacman`.
> More information: <https://manned.org/pacman.8>.

- List installed packages and versions:

`pacman -Q`

- List only packages and versions that were explicitly installed:

`pacman -Qe`

- Find which package owns a file:

`pacman -Qo {{filename}}`

- Display information about an installed package:

`pacman -Qi {{package}}`

- List files owned by a package:

`pacman -Ql {{package}}`

- List orphan packages (installed as dependencies but not required by any package):

`pacman -Qdtq`

- List installed packages not found in the repositories:

`pacman -Qm`

- List outdated packages:

`pacman -Qu`
