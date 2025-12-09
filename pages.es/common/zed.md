# zed

> Editor de texto diseñado para ser rápido, eficiente y cómodo.
> Más información: <https://zed.dev/docs/#cli>.

- Abre rutas específicas en Zed:

`zed {{ruta/al/archivo_o_directorio1 ruta/al/archivo_o_directorio2 ...}}`

- Abre una ruta en primer plano y muestra los registros:

`zed {{ruta/a/proyecto}} --foreground`

- Abre una ruta en una ventana nueva:

`zed {{ruta/al/proyecto}} {{[-n|--new]}}`

- Abre un archivo en el número de línea y columna dados:

`zed {{ruta/al/archivo}}:{{número_de_línea}}:{{número_de_columna}}`

- Abre una pestaña diff en Zed para dos versiones de un archivo:

`zed --diff {{ruta/a/archivo_antiguo}} {{ruta/al/archivo_nuevo}}`
