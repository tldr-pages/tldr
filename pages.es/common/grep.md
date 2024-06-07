# grep

> Encuentra patrones en archivos usando expresiones regulares.
> Más información: <https://www.gnu.org/software/grep/manual/grep.html>.

- Busca un patrón dentro de un archivo:

`grep "{{patrón_de_busqueda}}" {{ruta/al/archivo}}`

- Busca una cadena exacta (desactiva las expresiones regulares):

`grep --fixed-strings "{{cadena_exacta}}" {{ruta/al/archivo}}`

- Busca un patrón en todos los archivos de forma recursiva en un directorio, mostrando los números de línea de las coincidencias, ignorando los archivos binarios:

`grep --recursive --line-number --binary-files={{sin-parejamiento}} "{{patrón_de_búsqueda}}" {{ruta/al/directorio}}`

- Utiliza expresiones regulares extendidas (admite `?`, `+`, `{}`, `()` y `|`), sin distinguir entre mayúsculas y minúsculas:

`grep --extended-regexp --ignore-case " {{patrón_de_búsqueda}}" {{ruta/al/archivo}}`

- Imprime 3 líneas de contexto alrededor, antes o después de cada coincidencia:

`grep --{{context|before-context|after-context}}={{3}} "{{patrón_de_búsqueda}}" {{ruta/al/archivo}}`

- Imprime el nombre del archivo y el número de línea de cada coincidencia con salida en color:

`grep --with-filename --line-number --color=always "{{patrón_de_búsqueda}}" {{ruta/al/archivo}}`

- Busca líneas que coincidan con un patrón e imprime solo el texto coincidente:

`grep --only-matching "{{patrón_de_búsqueda}}" {{ruta/al/archivo}}`

- Busca `stdin` en las líneas que no coincidan con un patrón:

`cat {{ruta/al/archivo}} | grep --invert-match "{{patrón_de_busqueda}}"`
