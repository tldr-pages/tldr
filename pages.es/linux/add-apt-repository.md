# add-apt-repository

> Gestiona las definiciones de repositorios de `apt`.
> Más información: <https://manned.org/add-apt-repository>.

- Agrega un nuevo repositorio de `apt`:

`add-apt-repository {{especificación_del_repositorio}}`

- Elimina un repositorio de `apt`:

`add-apt-repository {{[-r|--remove]}} {{especificación_del_repositorio}}`

- Actualiza la caché de paquetes después de agregar un repositorio:

`add-apt-repository --update {{especificación_del_repositorio}}`

- Permite descargar paquetes fuente desde el repositorio:

`add-apt-repository {{[-s|--enable-source]}} {{especificación_del_repositorio}}`
