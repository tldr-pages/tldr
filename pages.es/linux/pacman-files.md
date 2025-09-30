# pacman --files

> Utilidad de manejo de paquetes de Arch Linux.
> Vea también: `pacman`, `pkgfile`.
> Más información: <https://manned.org/pacman.8>.

- Actualiza la base de datos de paquetes:

`sudo pacman -Fy`

- Encuentra el paquete que posee un archivo específico:

`pacman -F {{archivo}}`

- Encuentra el paquete que posee un archivo específico, utilizando una e[x]presión regular:

`pacman -Fx '{{expresión_regular}}'`

- Lista solo los nombres de los paquetes:

`pacman -Fq {{archivo}}`

- [L]ista los archivos que hacen parte de un paquete específico:

`pacman -Fl {{paquete}}`

- Muestra la ayuda:

`pacman -Fh`
