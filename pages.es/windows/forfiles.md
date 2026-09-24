# forfiles

> Selecciona archivos para ejecutar un comando especificado.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/forfiles>.

- Busca archivos en el directorio actual:

`forfiles`

- Busca archivos en un directorio específico:

`forfiles /p {{ruta\al\directorio}}`

- Ejecuta el comando especificado para cada archivo:

`forfiles /c "{{comando}}"`

- Busca archivos utilizando un patrón de glob específico:

`forfiles /m {{patrón_glob}}`

- Busca archivos de forma recursiva:

`forfiles /s`

- Busca archivos más antiguos que 5 días:

`forfiles /d +{{5}}`
