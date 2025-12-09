# airshare

> Transfiere datos entre dos máquinas en una red local.
> Más información: <https://airshare.rtfd.io/en/latest/cli.html>.

- Comparte archivos o directorios:

`airshare {{code}} {{ruta/al/archivo_o_directorio1 ruta/al/archivo_o_directorio2 ...}}`

- Recibe un archivo:

`airshare {{code}}`

- Aloja un servidor receptor (usa esto para poder cargar archivos usando la interfaz web):

`airshare --upload {{code}}`

- Envía archivos o directorios a un servidor receptor:

`airshare --upload {{code}} {{ruta/al/archivo_o_directorio1 ruta/al/archivo_o_directorio2 ...}}`

- Envía archivos cuyas rutas han sido copiadas al portapapeles:

`airshare --file-path {{code}}`

- Recibe un archivo y lo copia al portapapeles:

`airshare --clip-receive {{code}}`
