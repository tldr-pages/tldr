# mkfs.erofs

> Crea un sistema de archivos EROFS en una imagen.
> Más información: <https://manned.org/mkfs.erofs>.

- Crea un sistema de archivos EROFS basado en el directorio raíz:

`mkfs.erofs image.erofs root/`

- Crea una imagen EROFS con un UUID específico:

`mkfs.erofs -U {{UUID}} image.erofs root/`

- Crea una imagen EROFS comprimida:

`mkfs.erofs -zlz4hc image.erofs root/`

- Crea una imagen EROFS en la que todos los archivos pertenezcan a root:

`mkfs.erofs --all-root image.erofs root/`
