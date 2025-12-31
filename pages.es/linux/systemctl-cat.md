# systemctl cat

> Muestra el contenido completo de los archivos de unidad como los ve systemd.
> Más información: <https://www.freedesktop.org/software/systemd/man/systemctl.html#cat%20PATTERN%E2%80%A6>.

- Muestra el contenido y la ruta absoluta de un archivo de unidad:

`systemctl cat {{unidad}}`

- Muestra el contenido de múltiples archivos de unidad:

`systemctl cat {{unidad1 unidad2 ...}}`

- Muestra el contenido de un archivo de unidad para una plantilla:

`systemctl cat {{plantilla@}}`

- Muestra el contenido de un archivo de unidad de usuario:

`systemctl cat {{unidad}} --user`
