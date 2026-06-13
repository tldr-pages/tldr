# xcopy

> Copia archivos y árboles de directorios.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/xcopy>.

- Copia el o los archivos a la ubicación de destino especificada:

`xcopy {{ruta\al\archivo_o_directorio}} {{ruta\al\directorio_de_destino}}`

- Lista los archivos que se copiarán antes de copiarlos:

`xcopy {{ruta\al\archivo_o_directorio}} {{ruta\al\directorio_de_destino}} /p`

- Copiar solo la estructura del directorio, excluyendo archivos:

`xcopy {{ruta\al\archivo_o_directorio}} {{ruta\al\directorio_de_destino}} /t`

- Incluir directorios vacíos al copiar:

`xcopy {{ruta\al\archivo_o_directorio}} {{ruta\al\directorio_de_destino}} /e`

- Mantener el ACL de origen en el destino:

`xcopy {{ruta\al\archivo_o_directorio}} {{ruta\al\directorio_de_destino}} /o`

- Permitir reanudar cuando se pierde la conexión de red:

`xcopy {{ruta\al\archivo_o_directorio}} {{ruta\al\directorio_de_destino}} /z`

- Desactiva el aviso cuando el archivo existe en el destino:

`xcopy {{ruta\al\archivo_o_directorio}} {{ruta\al\directorio_de_destino}} /y`

- Muestra la ayuda:

`xcopy /?`
