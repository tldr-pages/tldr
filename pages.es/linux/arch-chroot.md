# arch-chroot

> Comando `chroot` mejorado para facilitar el proceso de instalación de Arch Linux.
> Más información: <https://manned.org/arch-chroot.8>.

- Inicia un intérprete de comandos interactivo (Bash por defecto) en un nuevo directorio raíz:

`arch-chroot {{ruta/al/nuevo/raiz}}`

- Especifica el usuario (distinto del actual) para ejecutar el intérprete de comandos:

`arch-chroot -u {{usuario}} {{ruta/al/nuevo/raiz}}`

- Ejecuta un comando personalizado (en lugar de Bash) en el nuevo directorio raíz:

`arch-chroot {{ruta/al/nuevo/raiz}} {{comando}} {{argumentos_del_comando}}`

- Especifica un intérprete de comandos distinto de Bash (en este caso, el paquete `zsh` debe estar instalado en el sistema de destino):

`arch-chroot {{ruta/al/nuevo/raiz}} {{zsh}}`
