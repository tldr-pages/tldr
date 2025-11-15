# add-apt-repository

> Gestiona les definicions dels repositoris APT.
> Més informació: <https://manned.org/add-apt-repository>.

- Afegeix un nou repositori APT:

`add-apt-repository {{especificacions_del_respositori}}`

- Elimina un repositori APT:

`add-apt-repository {{[-r|--remove]}} {{especificacions_del_repositori}}`

- Actualitza la memòria cau després d'afegir un repositori:

`add-apt-repository --update {{especificacions_del_repositori}}`

- Permet descarregar paquets font des del repositori:

`add-apt-repository {{[-s|--enable-source]}} {{especificacions_del_repositori}}`
