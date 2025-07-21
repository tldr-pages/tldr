# pacman --files

> Arch Linux package manager utility.
> See also: `pacman`, `pkgfile`.
> More information: <https://manned.org/pacman.8>.

- Update the package database:

`sudo pacman {{[-Fy|--files --refresh]}}`

- Find the package that owns a specific file:

`pacman {{[-F|--files]}} {{filename}}`

- Find the package that owns a specific file, using a regular expression:

`pacman {{[-Fx|--files --regex]}} '{{regular_expression}}'`

- List only the package names:

`pacman {{[-Fq|--files --quiet]}} {{filename}}`

- List the files owned by a specific package:

`pacman {{[-Fl|--files --list]}} {{package}}`

- Display help:

`pacman {{[-Fh|--files --help]}}`
