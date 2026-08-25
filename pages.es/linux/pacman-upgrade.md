# pacman --upgrade

> Instalar paquetes manualmente a partir de archivos comprimidos.
> Vea también: `pacman`.
> Más información: <https://manned.org/pacman.8>.

- Instala uno o más paquetes desde archivos:

`sudo pacman -U {{ruta/al/paquete1.pkg.tar.zst ruta/al/paquete2.pkg.tar.zst ...}}`

- Instala un paquete sin solicitar confirmación:

`sudo pacman -U --noconfirm {{ruta/al/paquete.pkg.tar.zst}}`

- Sobrescribe archivos conflictivos durante la instalación de un paquete:

`sudo pacman -U --overwrite {{ruta/al/archivo}} {{ruta/al/paquete.pkg.tar.zst}}`

- Instala un paquete, omitiendo las comprobaciones de versión de las dependencias:

`sudo pacman -Ud {{ruta/al/paquete.pkg.tar.zst}}`

- Obtiene e imprime los paquetes que se verían afectados por la actualización (no instala ningún paquete):

`pacman -Up {{ruta/al/paquete.pkg.tar.zst}}`

- Muestra la ayuda:

`pacman -Uh`
