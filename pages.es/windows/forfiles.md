# forfiles

> Seleccionar archivos para ejecutar un comando especificado.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/forfiles>.

- Buscar archivos en el directorio actual:

`forfiles`

- Buscar archivos en un directorio específico:

`forfiles /p {{ruta\al\directorio}}`

- Ejecutar el comando especificado para cada archivo:

`forfiles /c "{{comando}}"`

- Buscar archivos utilizando un patrón de glob específico:

`forfiles /m {{patrón_glob}}`

- Buscar archivos de forma recursiva:

`forfiles /s`

- Buscar archivos más antiguos que 5 días:

`forfiles /d +{{5}}`
