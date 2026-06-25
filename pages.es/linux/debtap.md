# debtap

> Convierte paquetes Debian en paquetes de Arch Linux.
> Vea también: `pacman-upgrade`.
> Más información: <https://github.com/helixarch/debtap#available-options>.

- Actualiza la base de datos de debtap (antes de la primera ejecución):

`sudo debtap {{[-u|--update]}}`

- Convierte el paquete especificado:

`debtap {{ruta/al/paquete.deb}}`

- Convierte el paquete especificado obviando todas las preguntas, excepto para editar archivos de metadatos:

`debtap {{[-q|--quiet]}} {{ruta/al/paquete.deb}}`

- Genera un archivo PKGBUILD:

`debtap {{[-p|--pkgbuild]}} {{ruta/al/paquete.deb}}`
