# add-apt-repository

> Gestionează definițiile de depozit apt.
> Mai multe informaţii: <https://manned.org/apt-add-repository>

- Adaugă un nou depozit apt:

`add-apt-repository {{repository_spec}}`

- Elimină un depozit apt:

`add-apt-repository --remove {{repository_spec}}`

- Actualizați memoria cache a pachetului după adăugarea unui depozit:

`add-apt-repository --update {{repository_spec}}`

- Activează pachetele sursă:

`add-apt-repository --enable-source {{repository_spec}}`
