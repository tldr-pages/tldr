# pacman --database

> Opera en la base de datos de paquetes de Arch Linux.
> Modifica ciertos atributos de los paquetes instalados.
> Vea también: `pacman`.
> Más información: <https://manned.org/pacman.8>.

- Marca un paquete como instalado implícitamente:

`sudo pacman -D --asdeps {{paquete}}`

- Marca un paquete como instalado explícitamente:

`sudo pacman -D --asexplicit {{paquete}}`

- Verifica que todas las dependencias del paquete estén instaladas:

`pacman -Dk`

- Verifica los repositorios para asegurarse de que todas las dependencias especificadas estén disponibles:

`pacman -Dkk`

- Muestra solo mensajes de error:

`pacman -Dkq`

- Muestra la ayuda:

`pacman -Dh`
