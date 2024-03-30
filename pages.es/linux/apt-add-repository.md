# apt-add-repository

> Gestiona las definiciones del repositorio APT.
> Más información: <https://manpages.debian.org/latest/software-properties-common/apt-add-repository.1.html>.

- Añade un nuevo repositorio APT:

`apt-add-repository {{repositorio}}`

- Elimina un repositorio APT:

`apt-add-repository --remove {{repositorio}}`

- Actualiza la caché de paquetes tras añadir un repositorio:

`apt-add-repository --update {{repositorio}}`

- Activa las fuentes de paquetes:

`apt-add-repository --enable-source {{repositorio}}`
