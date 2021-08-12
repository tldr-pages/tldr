# pacman --query

> Arch Linux pachet manager utilitar.
> Mai multe informaţii: <https://man.archlinux.org/man/pacman.8>

- Lista pachetelor și versiunilor instalate:

`pacman --query`

- Lista numai pachetele și versiunile care au fost instalate în mod explicit:

`pacman --query --explicit`

- Găsiți ce pachet deține un fișier:

`pacman --query --owns {{filename}}`

- Afișează informații despre un pachet instalat:

`pacman --query --info {{package_name}}`

- Lista fișierelor deținute de un pachet:

`pacman --query --list {{package_name}}`

- Lista pachetelor orfane (instalate ca dependențe, dar nu sunt cerute de niciun pachet):

`pacman --query --unrequired --deps --quiet`

- Lista pachetelor instalate care nu sunt găsite în depozite:

`pacman --query --foreign`

- Lista pachetelor învechite:

`pacman --query --upgrades`
