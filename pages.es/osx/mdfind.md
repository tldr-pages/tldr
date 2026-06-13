# mdfind

> Lista los archivos que coinciden con una consulta dada.
> Más información: <https://keith.github.io/xcode-man-pages/mdfind.1.html>.

- Busca un archivo por su nombre:

`mdfind -name {{archivo}}`

- Busca un archivo por su contenido:

`mdfind "{{consulta}}"`

- Busca un archivo que contenga una cadena, en un directorio determinado:

`mdfind -onlyin {{directorio}} "{{consulta}}"`
