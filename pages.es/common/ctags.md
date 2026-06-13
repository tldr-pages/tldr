# ctags

> Genera un archivo de índice (o etiqueta) de objetos de lenguaje que se encuentran en los archivos de código fuente de muchos lenguajes de programación populares.
> Más información: <https://docs.ctags.io/en/latest/man/ctags.1.html>.

- Genera etiquetas para un solo archivo y las envía a un archivo llamado "tags" en el directorio actual, sobrescribiendo el archivo si existe:

`ctags {{ruta/al/archivo}}`

- Genera etiquetas para todos los archivos en el directorio actual y las envía a un archivo específico, sobrescribiendo el archivo si existe:

`ctags -f {{ruta/al/archivo}} *`

- Genera etiquetas para todos los archivos en el directorio actual y todos los subdirectorios:

`ctags --recurse`

- Genera etiquetas para un solo archivo y las envía con el número de línea inicial y el número de línea final en formato JSON:

`ctags --fields=+ne --output-format=json {{ruta/al/archivo}}`
