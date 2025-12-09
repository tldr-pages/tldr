# xzgrep

> Busca archivos posiblemente comprimidos con `xz`, `lzma`, `gzip`, `bzip2`, `lzop`, o `zstd` utilizando expresiones regulares.
> Vea también: `grep`.
> Más información: <https://manned.org/xzgrep>.

- Busca un patrón dentro de un archivo:

`xzgrep "{{patrón_de_búsqueda}}" {{ruta/al/archivo}}`

- Busca una cadena exacta (sin expresiones regulares):

`xzgrep --fixed-strings "{{cadena_exacta}}" {{ruta/al/archivo}}`

- Busca un patrón en todos los archivos mostrando los números de línea que coinciden:

`xzgrep --line-number "{{patrón_de_búsqueda}}" {{ruta/al/archivo}}`

- Utiliza expresiones regulares extendidas (soporta `?`, `+`, `{}`, `()` y `|`), sin diferenciar mayúsculas y minúsculas (case-insensitive):

`xzgrep --extended-regexp --ignore-case "{{patrón_de_búsqueda}}" {{ruta/al/archivo}}`

- Imprime 3 líneas de contexto alrededor, antes o después de cada coincidencia:

`xzgrep --{{context|before-context|after-context}}={{3}} "{{patrón_de_búsqueda}}" {{ruta/al/archivo}}`

- Imprime el nombre del archivo y número de línea para cada coincidencia en color:

`xzgrep --with-filename --line-number --color=always "{{patrón_de_búsqueda}}" {{ruta/al/archivo}}`

- Busca líneas que coincidan con un patrón, imprime solo el texto coincidente:

`xzgrep --only-matching "{{patrón_de_búsqueda}}" {{ruta/al/archivo}}`
