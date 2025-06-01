# attrib

> Muestra o cambia los atributos de archivos o directorios.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/attrib>.

- Mostrar todos los atributos establecidos de los archivos en el directorio actual:

`attrib`

- Mostrar todos los atributos establecidos de los archivos en un directorio específico:

`attrib {{ruta\al\directorio}}`

- Mostrar todos los atributos establecidos de archivos y [d]irectorios en el directorio actual:

`attrib /d`

- Mostrar todos los atributos establecidos de los archivos en el directorio actual y [s]ubdirectorios:

`attrib /s`

- Agregar el atributo `solo-lectu[r]a` o `[a]rchivo` o `[s]istema` o `oculto[h]` o `contenido no [i]ndexado` a archivos o directorios:

`attrib +{{r|a|s|h|i}} {{ruta\al\archivo_o_directorio1 ruta\al\archivo_o_directorio2 ...}}`

- Eliminar un atributo específico de archivos o directorios:

`attrib -{{r|a|s|h|i}} {{ruta\al\archivo_o_directorio1 ruta\al\archivo_o_directorio2 ...}}`
