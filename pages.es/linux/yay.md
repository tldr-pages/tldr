# yay

> Yet Another Yogurt: crea e instala paquetes desde el repositorio de usuarios de Arch.
> Vea también `pacman`.
> Más información: <https://github.com/Jguer/yay#first-use>.

- Busca e instala paquetes de forma interactiva desde los repositorios y AUR:

`yay {{nombre_del_paquete|término_de_búsqueda}}`

- Sincroniza y actualiza todos los paquetes desde los repositorios y AUR:

`yay`

- Sincroniza y actualiza solo paquetes del AUR:

`yay -Sua`

- Instala un nuevo paquete desde los repositorios y AUR:

`yay -S {{paquete}}`

- Elimina un paquete instalado, sus dependencias y archivos de configuración:

`yay -Rns {{paquete}}`

- Busca en la base de datos de paquetes una palabra clave de los repositorios y AUR:

`yay -Ss {{palabra_clave}}`

- Elimina paquetes huérfanos (instalados como dependencias pero no requeridos por ningún paquete):

`yay -Yc`

- Muestra estadísticas de paquetes instalados y estado del sistema:

`yay -Ps`
