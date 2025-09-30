# bootc switch

> Apunta a una nueva referencia de imagen contenedora para arrancar.
> Más información: <https://manned.org/bootc-switch.8>.

- Cambia el SO base a una nueva imagen de contenedor desde un registro:

`sudo bootc switch {{imagen}}`

- Cambia el SO base a una nueva imagen de contenedor desde el almacenamiento local de imágenes del usuario root:

`sudo bootc switch --transport containers-storage {{imagen}}`

- Cambia el SO base a una nueva imagen contenedor almacenada en un tarball:

`sudo bootc switch --transport oci-archive {{ruta/a/imagen.tar.gz}}`
