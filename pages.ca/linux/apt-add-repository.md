# apt-add-repository

> Gestiona les definicions del repositori apt.
> Més informació: <https://manpages.debian.org/latest/software-properties-common/apt-add-repository.1.html>.

- Afegeix un nou repositori apt:

`apt-add-repository {{repositori}}`

- Elimina un repositori apt:

`apt-add-repository --remove {{repositori}}`

- Actualiza la memoria cau de paquets després d'afegir un repositori:

`apt-add-repository --update {{repositori}}`

- Activar les fonts de paquets:

`apt-add-repository --enable-source {{repositori}}`
