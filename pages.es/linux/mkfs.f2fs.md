# mkfs.f2fs

> Crea un sistema de archivos F2FS en una partición.
> Más información: <https://manned.org/mkfs.f2fs>.

- Crea un sistema de archivos F2FS en la primera partición del dispositivo b (`sdb1`):

`sudo mkfs.f2fs {{/dev/sdb1}}`

- Crea un sistema de archivos F2FS con una etiqueta de volumen:

`sudo mkfs.f2fs -l {{etiqueta_volumen}} {{/dev/sdb1}}`
