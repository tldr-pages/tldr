# pacman --sync

> Utilidad del administrador de paquetes de Arch Linux.
> Vea también: `pacman`.
> Más información: <https://manned.org/pacman.8>.

- Instala un paquete nuevo:

`sudo pacman -S {{paquete}}`

- [S]incroniza y actualiza ([y]) la base de datos de paquetes junto con un sys[u]pgrade (añade `--downloadonly` para solamente descargar los paquetes y no actualizarlos):

`sudo pacman -Syu`

- Actualiza (update) y moderniza ([u]pgrade) todos los paquetes e instala uno nuevo sin solicitar confirmación:

`sudo pacman -Syu --noconfirm {{paquete}}`

- Busca ([s]) la base de datos de paquetes con una expresión regular o palabra clave:

`pacman -Ss "{{patrón_de_búsqueda}}"`

- Muestra [i]nformación sobre un paquete:

`pacman -Si {{paquete}}`

- Sobrescribe archivos conflictivos durante una actualización del paquete:

`sudo pacman -Syu --overwrite {{ruta/al/archivo}}`

- [S]incroniza y act[u]aliza todos los paquetes, e ignora un paquete específico (puede ser utilizado más de una vez):

`sudo pacman -Syu --ignore {{paquete1 paquete2 ...}}`

- Elimina paquetes no instalados y repositorios no utilizados de la caché (utiliza las banderas `Sc` para limpiar ([c]) todos los paquetes):

`sudo pacman -Sc`
