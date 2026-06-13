# sort

> Ordena líneas de archivos de texto.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/sort-invocation.html>.

- Ordena un archivo en orden ascendente:

`sort {{ruta/al/archivo}}`

- Ordena un archivo en orden descendente:

`sort {{[-r|--reverse]}} {{ruta/al/archivo}}`

- Ordena un archivo sin distinguir entre mayúsculas y minúsculas:

`sort {{[-f|--ignore-case]}} {{ruta/al/archivo}}`

- Ordena un archivo usando orden numérico en lugar de alfabético:

`sort {{[-n|--numeric-sort]}} {{ruta/al/archivo}}`

- Ordena `/etc/passwd` por el tercer campo de cada línea numéricamente, usando `:` como separador de campos:

`sort {{[-t|--field-separator]}} : {{[-k|--key]}} 3n /etc/passwd`

- Como el anterior, pero cuando los elementos del tercer campo son iguales, ordena por el cuarto campo con números con exponentes:

`sort {{[-t|--field-separator]}} : {{[-k|--key]}} 3,3n {{[-k|--key]}} 4,4g /etc/passwd`

- Ordena un archivo conservando únicamente las líneas únicas:

`sort {{[-u|--unique]}} {{ruta/al/archivo}}`

- Ordena un archivo, imprimiendo la salida en un archivo específico (puede usarse para ordenar un archivo en el sitio):

`sort {{[-o|--output]}} {{ruta/al/archivo_de_salida}} {{ruta/al/archivo_de_entrada}}`
