# pacman --remove

> Arch Linux pachet manager utilitar.
> Mai multe informaţii: <https://man.archlinux.org/man/pacman.8>

- Afișează ajutor pentru această subcomandă:

`pacman --remove --help`

- Eliminați un pachet și dependențele sale:

`sudo pacman --remove --recursive {{package_name}}`

- Eliminați un pachet și atât dependențele sale și fișierele de configurare:

`sudo pacman --remove --recursive --nosave {{package_name}}`

- Eliminați un pachet fără a solicita:

`sudo pacman --remove --noconfirm {{package_name}}`

- Eliminați pachetele orfane (instalate ca dependențe, dar nu sunt cerute de niciun pachet):

`sudo pacman --remove --recursive --nosave $(pacman --query --unrequired --deps --quiet)`

- Eliminați un pachet și toate pachetele care depind de el:

`sudo pacman --remove --cascade {{package_name}}`

- Lista pachetelor care ar fi afectate (nu elimină niciun pachet):

`pacman --remove --print {{package_name}}`
