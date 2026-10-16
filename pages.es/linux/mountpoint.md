# mountpoint

> Comprueba si un directorio es un punto de montaje de un sistema de archivos.
> Más información: <https://manned.org/mountpoint>.

- Comprueba si un directorio es un punto de montaje:

`mountpoint {{ruta/al/directorio}}`

- Comprueba si un directorio es un punto de montaje sin mostrar ninguna salida:

`mountpoint {{[-q|--quiet]}} {{ruta/al/directorio}}`

- Muestra los números mayor/menor del sistema de archivos de un punto de montaje:

`mountpoint {{[-d|--fs-devno]}} {{ruta/al/directorio}}`
