# diskutil

> Utilidad para gestionar discos y volúmenes locales.
> Más información: <https://keith.github.io/xcode-man-pages/diskutil.8.html>.

- Lista todos los discos, particiones y volúmenes montados actualmente disponibles:

`diskutil list`

- Repara las estructuras de datos del sistema de archivos de un volumen:

`diskutil repairVolume {{/dev/disk_device}}`

- Desmonta un volumen:

`diskutil unmountDisk {{/dev/disk_device}}`

- Expulsa un CD/DVD (primero lo desmonta):

`diskutil eject {{/dev/disk_device1}}`
