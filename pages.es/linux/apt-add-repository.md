# apt-add-repository

> Gestiona las definiciones del repositorio apt.
> Más información: <https://manpages.debian.org/latest/software-properties-common/apt-add-repository.1.html>.

- Añade un nuevo repositorio apt:

`apt-add-repository {{repositorio}}`

- Elimina un repositorio apt:

`apt-add-repository --remove {{repositorio}}`

- Actualiza la caché de paquetes tras añadir un repositorio:

`apt-add-repository --update {{repositorio}}`

- Activa las fuentes de paquetes:

`apt-add-repository --enable-source {{repositorio}}`
