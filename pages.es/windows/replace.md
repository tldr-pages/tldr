# replace

> Reemplaza archivos.
> Ver también: `robocopy`, `move`, `copy` y `del`.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/replace>.

- Reemplazar el archivo de destino con el del directorio origen:

`replace {{ruta\al\archivo_o_directorio}} {{ruta\al\directorio_destino}}`

- Agregar archivos al directorio destino en lugar de reemplazar archivos existentes:

`replace {{ruta\al\archivo_o_directorio}} {{ruta\al\directorio_destino}} /a`

- Copiar múltiples archivos de forma interactiva, con una solicitud antes de reemplazar o agregar un archivo destino:

`replace {{ruta\al\archivo_o_directorio}} {{ruta\al\directorio_destino}} /p`

- Reemplazar incluso archivos de solo lectura:

`replace {{ruta\al\archivo_o_directorio}} {{ruta\al\directorio_destino}} /r`

- Esperar a que insertes un disco antes de reemplazar archivos (originalmente para permitir insertar un disquete):

`replace {{ruta\al\archivo_o_directorio}} {{ruta\al\directorio_destino}} /w`

- Reemplazar todos los archivos en subdirectorios del destino:

`replace {{ruta\al\archivo_o_directorio}} {{ruta\al\directorio_destino}} /s`

- Reemplazar solo los archivos en el directorio destino que sean más antiguos que los archivos en el directorio origen:

`replace {{ruta\al\archivo_o_directorio}} {{ruta\al\directorio_destino}} /u`

- Mostrar ayuda:

`replace /?`
