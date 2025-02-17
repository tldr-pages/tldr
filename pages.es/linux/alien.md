# alien

> Convierte diferentes paquetes de instalación a otros formatos.
> Vea también: `debtap`, para la conversión de `.deb` en Arch Linux.
> Más información: <https://manned.org/alien>.

- Convierte un archivo de instalación específico al formato Debian (extensión `.deb`):

`sudo alien --to-deb {{ruta/al/archivo}}`

- Convierte un archivo de instalación específico al formato Red Hat (extensión `.rpm`):

`sudo alien --to-rpm {{ruta/al/archivo}}`

- Convierte un archivo de instalación específico al formato de instalación de Slackware (extensión `.tgz`):

`sudo alien --to-tgz {{ruta/al/archivo}}`

- Convierte un archivo de instalación específico al formato Debian y lo instala en el sistema:

`sudo alien --to-deb --install {{ruta/al/archivo}}`
