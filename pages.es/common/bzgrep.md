# bzgrep

> Encuentra patrones en archivos comprimidos `bzip2` usando `grep`.
> Más información: <https://manned.org/bzgrep>.

- Busca un patrón dentro de un archivo comprimido:

`bzgrep "{{patrón_de_búsqueda}}" {{ruta/al/archivo}}`

- Busca un patrón de forma recursiva en un archivo comprimido bzip2 `.tar`:

`bzgrep {{[-r|--recursive]}} "{{patrón_de_búsqueda}}" {{ruta/a/archivo_tar}}`

- Imprime 3 líneas de [C]ontexto alrededor, [A]ntes o [D]espués de cada coincidencia:

`bzgrep {{--context|--before-context|--after-context}} 3 "{{patrón_de_búsqueda}}" {{ruta/al/archivo}}`

- Imprime el nombre del archivo y el número de línea de cada coincidencia:

`bzgrep {{[-H|--with-filename]}} {{[-n|--line-number]}} "{{patrón_de_búsqueda}}" {{ruta/al/archivo}}`

- Busca líneas que coincidan con un patrón, imprimiendo solo el texto coincidente:

`bzgrep {{[-o|--only-matching]}} "{{patrón_de_búsqueda}}" {{ruta/al/archivo}}`

- Busca en `stdin` líneas que no coincidan con un patrón:

`cat {{ruta/al/archivo_comprimido}} | bzgrep {{[-v|--invert-match]}} "{{patrón_de_búsqueda}}"`

- Utiliza `regex` extendida (admite `?`, `+`, `{}`, `()` y `|`), sin distinguir mayúsculas de minúsculas:

`bzgrep {{[-E|--extended-regexp]}} {{[-i|--ignore-case]}} "{{patrón_de_búsqueda}}" {{ruta/al/archivo}}`
