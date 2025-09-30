# grep

> Encuentra patrones en archivos usando expresiones regulares.
> Más información: <https://www.gnu.org/software/grep/manual/grep.html>.

- Busca un patrón en un archivo:

`grep "{{patrón_de_búsqueda}}" {{ruta/al/archivo}}`

- Busca una cadena de caracteres específica (la cadena no será interpretada como una expresión regular):

`grep {{[-F|--fixed-strings]}} "{{cadena_exacta}}" {{ruta/al/archivo}}`

- Busca un patrón en todos los archivos de forma recursiva en un directorio, mostrando los números de línea de las coincidencias e ignorando los archivos binarios:

`grep {{[-rnI|--recursive --line-number --binary-files=without-match]}} "{{patrón_de_búsqueda}}" {{ruta/al/directorio}}`

- Utiliza expresiones regulares extendidas (los metacaracteres `?`, `+`, `{}`, `()` y `|` no requieren de una barra inversa), sin distinguir entre mayúsculas y minúsculas:

`grep {{[-Ei|--extended-regexp --ignore-case]}} "{{patrón_de_búsqueda}}" {{ruta/al/archivo}}`

- Imprime 3 líneas alrededor, antes o después de cada coincidencia:

`grep {{--context|--before-context|--after-context}} 3 "{{patrón_de_búsqueda}}" {{ruta/al/archivo}}`

- Imprime con colores el nombre del archivo y el número de línea de cada coincidencia:

`grep {{[-Hn|--with-filename --line-number]}} --color=always "{{patrón_de_búsqueda}}" {{ruta/al/archivo}}`

- Busca líneas que coincidan con un patrón e imprime solo el texto coincidente:

`grep {{[-o|--only-matching]}} "{{patrón_de_búsqueda}}" {{ruta/al/archivo}}`

- Busca líneas en`stdin` que no coincidan con el patrón:

`cat {{ruta/al/archivo}} | grep {{[-v|--invert-match]}} "{{patrón_de_busqueda}}"`
