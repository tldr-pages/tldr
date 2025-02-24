# add-apt-repository

> Gestiona las definiciones de repositorios de `apt`.
> Más información: <https://manned.org/apt-add-repository>.

- Agrega un nuevo repositorio de `apt`:

`add-apt-repository {{especificación_del_repositorio}}`

- Elimina un repositorio de `apt`:

`add-apt-repository --remove {{especificación_del_repositorio}}`

- Actualiza la caché de paquetes después de agregar un repositorio:

`add-apt-repository --update {{especificación_del_repositorio}}`

- Permite descargar paquetes fuente desde el repositorio:

`add-apt-repository --enable-source {{especificación_del_repositorio}}`
