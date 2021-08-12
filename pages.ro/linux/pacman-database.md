# pacman --database

> Opera pe baza de date pachet Arch Linux.
> Modificați anumite atribute ale pachetelor instalate.
> Mai multe informaţii: <https://man.archlinux.org/man/pacman.8>

- Ajutor pentru afișare:

`pacman --database --help`

- Marcați un pachet ca implicit instalat:

`sudo pacman --database --asdeps {{package_name}}`

- Marcați un pachet ca fiind instalat în mod explicit:

`sudo pacman --database --asexplicit {{package_name}}`

- Verificați dacă toate dependențele pachetelor sunt instalate:

`pacman --database --check`

- Verificați depozitele pentru a vă asigura că toate dependențele specificate sunt disponibile:

`pacman --database --check --check`

- Afișează numai mesaje de eroare:

`pacman --database --check --quiet`
