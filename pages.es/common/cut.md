# cut

> Recorta campos provenientes de la entrada estándar o de archivos.
> Más información: <https://www.gnu.org/software/coreutils/cut>.

- Recorta los primeros 16 caracteres de cada línea de la entrada estándar:

`cut -c {{1-16}}`

- Recorta los primeros 16 caracteres de cada línea de los archivos especificados:

`cut -c {{1-16}} {{archivo}}`

- Recorta todo desde el tercer caracter hasta el final de cada línea:

`cut -c {{3-}}`

- Recorta el quinto campo de cada línea, usando los dos puntos como delimitadores de campos (por defecto el delimitador es tab):

`cut -d'{{:}}' -f{{5}}`

- Recorta el segundo y décimo campo de cada línea, usando los punto y coma como delimitadores:

`cut -d'{{;}}' -f{{2,10}}`

- Recorta los campos del tercero al último de cada línea, usando los espacios como delimintadores:

`cut -d'{{ }}' -f{{3-}}`
