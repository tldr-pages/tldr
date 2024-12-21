# pkgfile

> Busca archivos en los paquetes de los repositorios oficiales en sistemas basados en Arch.
> Vea también: `pacman files`, que describe el uso de `pacman --files`.
> Más información: <https://manned.org/pkgfile>.

- Sincroniza la base de datos pkgfile:

`sudo pkgfile --update`

- Busca un paquete que posee un archivo específico:

`pkgfile {{archivo}}`

- Lista todos los archivos proporcionados por un paquete:

`pkgfile --list {{paquete}}`

- Lista los ejecutables proporcionados por un paquete:

`pkgfile --list --binaries {{paquete}}`

- Busca un paquete que posee un archivo específico utilizando coincidencias insensibles a mayúsculas y minúsculas:

`pkgfile --ignorecase {{archivo}}`

- Busca un paquete que posee un archivo específico en el directorio `bin` o `sbin`:

`pkgfile --binaries {{archivo}}`

- Busca un paquete que posee un archivo específico, mostrando la versión del paquete:

`pkgfile --verbose {{archivo}}`

- Busca un paquete que posee un archivo específico en un repositorio específico:

`pkgfile --repo {{nombre_del_repositorio}} {{archivo}}`
