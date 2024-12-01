# pacman --remove

> Utilidad del administrador de paquetes de Arch Linux.
> Vea también: `pacman`.
> Más información: <https://manned.org/pacman.8>.

- [R]emueve un paquete y sus dependencias recur[s]ivamente:

`sudo pacman -Rs {{paquete}}`

- [R]emueve un paquete y sus dependencias. [n]o guarda copias de seguridad de los archivos de configuración:

`sudo pacman -Rsn {{paquete}}`

- [R]emueve un paquete sin pedir confirmación:

`sudo pacman -R --noconfirm {{paquete}}`

- [R]emueve los paquetes huérfanos (instalados como [d]ependencias pero no requeridos por algún paquete):

`sudo pacman -Rsn $(pacman -Qdtq)`

- [R]emueve un paquete y ha[c]e lo mismo a todos los paquetes que dependen de él:

`sudo pacman -Rc {{paquete}}`

- Lista e im[p]rime los paquetes que serían afectados (no [R]emueve paquete alguno):

`pacman -Rp {{paquete}}`

- Muestra la ayuda:

`pacman -Rh`
