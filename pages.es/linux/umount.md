# umount

> Desvincula un sistema de archivos de su punto de montaje, haciendo que deje de ser accesible.
> Un sistema de archivos no se puede desmontar mientras está en uso.
> Más información: <https://manned.org/umount.8>.

- Desmonta un sistema de archivos indicando la ruta del origen desde el que está montado:

`sudo umount {{ruta/al/archivo_de_dispositivo}}`

- Desmonta un sistema de archivos indicando la ruta del destino donde está montado:

`sudo umount {{ruta/al/directorio_montado}}`

- Si el desmontaje falla, intenta volver a montar el sistema de archivos en modo de solo lectura:

`sudo umount {{[-r|--read-only]}} {{ruta/al/directorio_montado}}`

- Desmonta recursivamente cada directorio indicado:

`sudo umount {{[-R|--recursive]}} {{ruta/al/directorio_montado}}`

- Desmonta todos los sistemas de archivos montados (excepto el sistema de archivos `proc`):

`sudo umount {{[-a|--all]}}`

- Separa un sistema de archivos de la jerarquía de sistemas de archivos y lo desmonta en cuanto no haya referencias al mismo:

`sudo umount {{[-l|--lazy]}} {{ruta/al/directorio_montado}}`
