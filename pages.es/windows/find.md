# find

> Buscar una cadena especificada en archivos.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/find>.

- Buscar líneas que contengan una cadena especificada:

`find "{{cadena}}" {{ruta\al\archivo_o_directorio}}`

- Mostrar líneas que no contengan la cadena especificada:

`find "{{cadena}}" {{ruta\al\archivo_o_directorio}} /v`

- Mostrar el conteo de líneas que contienen la cadena especificada:

`find "{{cadena}}" {{ruta\al\archivo_o_directorio}} /c`

- Mostrar números de línea junto con la lista de líneas:

`find "{{cadena}}" {{ruta\al\archivo_o_directorio}} /n`
