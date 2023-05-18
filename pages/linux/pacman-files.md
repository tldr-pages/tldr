# pacman --files

> Arch Linux package manager utility.
> See also: `pacman`, `pkgfile`.
> More information: <https://man.archlinux.org/man/pacman.8>.

- Update the package database:

`sudo pacman --files --refresh`

- Find the package that owns a specific file:

`pacman --files {{filename}}`

- Find the package that owns a specific file, using a regular expression:

`pacman --files --regex '{{regular_expression}}'`

- List only the package names:

`pacman --files --quiet {{filename}}`

- List the files owned by a specific package:

`pacman --files --list {{package_name}}`

- Display help:

`pacman --files --help`
