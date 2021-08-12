# pacman --upgrade

> Arch Linux pachet manager utilitar.
> Mai multe informaţii: <https://man.archlinux.org/man/pacman.8>

- Ajutor pentru afișare:

`pacman --upgrade --help`

- Instalați unul sau mai multe pachete din fișiere:

`sudo pacman --upgrade {{path/to/package1.pkg.tar.zst}} {{path/to/package2.pkg.tar.zst}}`

- Instalați un pachet fără a solicita:

`sudo pacman --upgrade --noconfirm {{path/to/package.pkg.tar.zst}}`

- Suprascrie fișierele conflictuale în timpul unei instalări de pachete:

`sudo pacman --upgrade --overwrite {{path/to/file}} {{path/to/package.pkg.tar.zst}}`

- Instalați un pachet, sărind peste verificările versiunii de dependență:

`sudo pacman --upgrade --nodeps {{path/to/package.pkg.tar.zst}}`

- Lista pachetelor care ar fi afectate (nu instalează pachete):

`pacman --query --print {{path/to/package.pkg.tar.zst}}`
