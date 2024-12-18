# pacman --query

> Arch Linux package manager utility.
> See also: `pacman`.
> More information: <https://manned.org/pacman.8>.

- [Q]uery the local package database and list installed packages and versions:

`pacman -Q`

- List only packages and versions that were [e]xplicitly installed:

`pacman -Qe`

- Find which package [o]wns a file:

`pacman -Qo {{filename}}`

- Display information about an [i]nstalled package:

`pacman -Qi {{package}}`

- [L]ist files owned by a package:

`pacman -Ql {{package}}`

- List orphan packages (installed as [d]ependencies but unrequired by any package without errors displayed):

`pacman -Qdtq`

- List installed packages not found in the repositories:

`pacman -Qm`

- List packages that can be [u]pgraded:

`pacman -Qu`
