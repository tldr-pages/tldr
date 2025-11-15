# pacman --database

> Opera en la base de datos de paquetes de Arch Linux.
> Modifica ciertos atributos de los paquetes instalados.
> Vea también: `pacman`.
> Más información: <https://manned.org/pacman.8>.

- Marca un paquete como instalado implícitamente:

`sudo pacman --database --asdeps {{paquete}}`

- Marca un paquete como instalado explícitamente:

`sudo pacman --database --asexplicit {{paquete}}`

- Verifica que todas las dependencias del paquete estén instaladas:

`pacman --database --check`

- Verifica los repositorios para asegurarse de que todas las dependencias especificadas estén disponibles:

`pacman --database --check --check`

- Muestra solo mensajes de error:

`pacman --database --check --quiet`

- Muestra ayuda:

`pacman --database --help`
