# pacman

> Arch Linux paquete manager utility.
> Utilidad del administrador de paquetes de Arch Linux.
> Vea también: `pacman-sync`, `pacman-remove`, `pacman-query`, `pacman-upgrade`, `pacman-files`, `pacman-database`, `pacman-deptest`, `pacman-key`, `pacman-mirrors`.
> Para comandos equivalentes en otros administradores de paquetes, vea <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> Más información: <https://manned.org/pacman.8>.

- Sincroniza y actualiza todos los paquetes:

`sudo pacman -Syu`

- Instala un nuevo paquete:

`sudo pacman -S {{paquete}}`

- Elimina un paquete y sus dependencias:

`sudo pacman -Rs {{paquete}}`

- Busca en la base de datos paquetes que contengan un archivo específico:

`pacman -F "{{nombre_del_archivo}}"`

- Lista los paquetes y versiones instalados:

`pacman -Q`

- Lista solo los paquetes y versiones instalados explícitamente:

`pacman -Qe`

- Lista los paquetes huérfanos (instalados como dependencias pero que en realidad no son necesarios para ningún paquete):

`pacman -Qtdq`

- Vacía toda la caché de `pacman`:

`sudo pacman -Scc`
