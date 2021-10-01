# grep

> Encuentra coincidencias en el texto introducido.
> Soporta patrones simples y expresiones regulares.
> Más información: <https://www.gnu.org/software/grep/manual/grep.html>.

- Busca un patrón dentro de un archivo:

`grep {{patron}} {{ruta/al/archivo}}`

- Busca un patrón exacto:

`grep -F {{patron_exacto}} {{ruta/al/archivo}}`

- Busca un patrón [R]ecursivamente en el directorio actual, mostrando los correspondientes [n]úmeros de línea, [I]gnorando archivos binarios:

`grep -RIn {{patron}} .`

- Usa expresiones regulares extendidas (soportando `?`, `+`, `{}`, `()` y `|`), sin importar mayúsculas o minúsculas:

`grep -Ei {{patron}} {{ruta/al/archivo}}`

- Imprime 3 líneas de [C]ontexto alrededor, anteriores ([B]), o posteriores ([A]) tras la coincidencia:

`grep -{{C|B|A}} 3 {{patron}} {{ruta/al/archivo}}`

- Imprime el nombre del archivo con la línea correspondiente a cada coincidencia:

`grep -Hn {{patron}} {{ruta/al/archivo}}`

- Usa la entrada estándar en vez de un archivo:

`cat {{ruta/al/archivo}} | grep {{patron}}`

- Encuentra coincidencias in[v]ersas al patrón (aquellas líneas que no lo contengan):

`grep -v {{patron}}`
