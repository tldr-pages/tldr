# pacman --files

> Arch Linux pachet manager utilitar.
> A se vedea, de asemenea, `pkgfile`.
> Mai multe informaţii: <https://man.archlinux.org/man/pacman.8>

- Ajutor pentru afișare:

`pacman --files --help`

- Actualizați baza de date a pachetelor:

`sudo pacman --files --refresh`

- Găsiți pachetul care deține un anumit fișier:

`pacman --files {{filename}}`

- Găsiți pachetul care deține un anumit fișier, folosind o expresie regulată:

`pacman --files --regex '{{regular_expression}}'`

- Listează numai numele pachetelor:

`pacman --files --quiet {{filename}}`

- Listează fișierele deținute de un anumit pachet:

`pacman --files --list {{package_name}}`

- Listați numai calea absolută către fișiere:

`pacman --query --list --quiet {{package_name}}`
