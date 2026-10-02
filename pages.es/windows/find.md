# find

> Busca una cadena especificada en archivos.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/find>.

- Busca líneas que contengan una cadena especificada:

`find "{{cadena}}" {{ruta\al\archivo_o_directorio}}`

- Muestra líneas que no contengan la cadena especificada:

`find "{{cadena}}" {{ruta\al\archivo_o_directorio}} /v`

- Muestra el conteo de líneas que contienen la cadena especificada:

`find "{{cadena}}" {{ruta\al\archivo_o_directorio}} /c`

- Muestra números de línea junto con la lista de líneas:

`find "{{cadena}}" {{ruta\al\archivo_o_directorio}} /n`
