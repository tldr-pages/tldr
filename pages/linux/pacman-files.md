# pacman -F

> Arch Linux package manager utility.
> See also: `pacman`, `pkgfile`.
> More information: <https://manned.org/pacman.8>.

- Update the package database:

`sudo pacman -Fy`

- Find the package that owns a specific file:

`pacman -F {{filename}}`

- Find the package that owns a specific file, using a regular e[x]pression:

`pacman -Fx '{{regular_expression}}'`

- List only the package names:

`pacman -Fq {{filename}}`

- Give the [l]ist of files owned by a specific package:

`pacman -Fl {{package}}`

- Display [h]elp:

`pacman -Fh`
