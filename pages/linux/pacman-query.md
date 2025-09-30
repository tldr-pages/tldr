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

- Display the [l]ist of files owned by a specific package:

`pacman -Ql {{package}}`

- List orphan packages (installed as [d]ependencies but unrequired ([t]) by any package and print in [q]uiet mode (only package name is displayed)):

`pacman -Qdtq`

- List installed packages foreign ([m]) to the repository database:

`pacman -Qm`

- List packages that can be [u]pgraded:

`pacman -Qu`
