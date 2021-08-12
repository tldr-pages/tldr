# pacman

> Arch Linux pachet manager utilitar.
> Mai multe informaţii: <https://man.archlinux.org/man/pacman.8>

- Sincronizați și actualizați toate pachetele:

`pacman --sync --refresh --sysupgrade`

- Instalați un pachet nou:

`pacman --sync {{package_name}}`

- Eliminați un pachet și dependențele sale:

`pacman --remove --recursive {{package_name}}`

- Căutați în baza de date a pachetelor o expresie sau un cuvânt cheie regulat:

`pacman --sync --search "{{search_pattern}}"`

- Lista pachetelor și versiunilor instalate:

`pacman --query`

- Listează numai pachetele și versiunile instalate în mod explicit:

`pacman --query --explicit`

- Lista pachetelor orfane (instalate ca dependențe, dar nu sunt cerute de niciun pachet):

`pacman --query --unrequired --deps --quiet`

- Goliţi întreaga memorie cache Pacman:

`pacman --sync --clean --clean`
