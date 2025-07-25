# pacman --files

> Arch Linux package manager utility.
> See also: `pacman`, `pkgfile`.
> More information: <https://manned.org/pacman.8>.

- Update the package database:

`sudo pacman -Fy`

- Find the package that owns a specific [F]ile:

`pacman -F {{filename}}`

- Find the package that owns a specific [F]ile, using a `rege[x]`:

`pacman -Fx '{{regex}}'`

- List only the package names:

`pacman -Fq {{filename}}`

- [l]ist the [F]iles owned by a specific package:

`pacman -Fl {{package}}`

- Display [h]elp:

`pacman -Fh`
