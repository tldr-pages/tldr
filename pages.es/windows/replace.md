# replace

> Reemplaza archivos.
> Ver también: `robocopy`, `move`, `copy` y `del`.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/replace>.

- Reemplaza el archivo de destino con el del directorio origen:

`replace {{ruta\al\archivo_o_directorio}} {{ruta\al\directorio_destino}}`

- Agrega archivos al directorio destino en lugar de reemplazar archivos existentes:

`replace {{ruta\al\archivo_o_directorio}} {{ruta\al\directorio_destino}} /a`

- Copia múltiples archivos de forma interactiva, con una solicitud antes de reemplazar o agregar un archivo destino:

`replace {{ruta\al\archivo_o_directorio}} {{ruta\al\directorio_destino}} /p`

- Reemplaza incluso archivos de solo lectura:

`replace {{ruta\al\archivo_o_directorio}} {{ruta\al\directorio_destino}} /r`

- Espera a que insertes un disco antes de reemplazar archivos (originalmente para permitir insertar un disquete):

`replace {{ruta\al\archivo_o_directorio}} {{ruta\al\directorio_destino}} /w`

- Reemplaza todos los archivos en subdirectorios del destino:

`replace {{ruta\al\archivo_o_directorio}} {{ruta\al\directorio_destino}} /s`

- Reemplaza solo los archivos en el directorio destino que sean más antiguos que los archivos en el directorio origen:

`replace {{ruta\al\archivo_o_directorio}} {{ruta\al\directorio_destino}} /u`

- Muestra la ayuda:

`replace /?`
