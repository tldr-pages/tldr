# apt-add-repository

> Gestionează definițiile de depozit apt.
> Mai multe informaţii: <https://manpages.debian.org/latest/software-properties-common/apt-add-repository.1.html>

- Adaugă un nou depozit apt:

`apt-add-repository {{repository_spec}}`

- Elimină un depozit apt:

`apt-add-repository --remove {{repository_spec}}`

- Actualizați memoria cache a pachetului după adăugarea unui depozit:

`apt-add-repository --update {{repository_spec}}`

- Activează pachetele sursă:

`apt-add-repository --enable-source {{repository_spec}}`
