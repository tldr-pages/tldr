# paccache

> Una utilidad de limpieza de caché de `pacman`.
> Más información: <https://manned.org/paccache>.

- Elimina todas las versiones de paquetes de `pacman` excepto las últimas 3:

`paccache {{[-r|--remove]}}`

- Define el número de versiones de paquetes para conservar:

`paccache {{[-rk|--remove --keep]}} {{número_de_versiones}}`

- Realiza una ejecución-en-seco y muestra el número de paquetes candidatos a ser eliminados:

`paccache {{[-d|--dryrun]}}`

- Mueve los paquetes candidatos a un directorio en lugar de eliminarlos:

`paccache {{[-m|--move]}} {{ruta/al/directorio}}`
