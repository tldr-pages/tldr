# systemd-dissect

> Analiza e interactúa con el sistema de archivos correspondientes a imágenes de disco de sistemas operativos, concretamente con imágenes de disco detectables (DDI).
> Más información: <https://www.freedesktop.org/software/systemd/man/latest/systemd-dissect.html>.

- Muestra información general sobre la imagen del sistema operativo:

`systemd-dissect {{ruta/a/imagen.raw}}`

- Monta una imagen del sistema operativo:

`systemd-dissect {[-m|--mount]} {{ruta/a/imagen.raw}} {{/mnt/imagen}}`

- Desmonta una imagen del sistema operativo:

`systemd-dissect {{[-u|--umount]}} {{/mnt/image}}`

- Muestra una lista de los archivos de una imagen:

`systemd-dissect {{[-l|--list]}} {{ruta/a/imagen.raw}}`

- Adjunta una imagen del sistema operativo a un dispositivo de bloque de bucle invertido asignado automáticamente e imprime su ruta:

`systemd-dissect --attach {{ruta/a/imagen.raw}}`

- Desconecta una imagen del sistema operativo de un dispositivo de bloque de bucle invertido:

`systemd-dissect --detach {{ruta/al/dispositivo}}`
