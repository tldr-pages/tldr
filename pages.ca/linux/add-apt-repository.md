# add-apt-repository

> Gestiona les definicions dels repositoris apt.
> Més informació: <https://manned.org/apt-add-repository>.

- Afegeix un nou repositori apt:

`add-apt-repository {{especificacions_del_respositori}}`

- Elimina un repositori apt:

`add-apt-repository --remove {{especificacions_del_repositori}}`

- Actualitza la memòria cau després d'afegir un repositori:

`add-apt-repository --update {{especificacions_del_repositori}}`

- Permet descarregar paquets font des del repositori:

`add-apt-repository --enable-source {{especificacions_del_repositori}}`
