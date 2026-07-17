# csplit

> Divide un archivo en partes.
> Esto genera archivos con los nombres `xx00`, `xx01`, y así sucesivamente.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/csplit-invocation.html>.

- Divide un archivo en dos partes, comenzando la segunda en la línea 10:

`csplit {{ruta/al/archivo}} 10`

- Divide un archivo en tres partes, comenzando las últimas partes en las líneas 7 y 23:

`csplit {{ruta/al/archivo}} 7 23`

- Inicia una nueva parte cada 5 líneas (fallará si el número de líneas no es divisible por 5):

`csplit {{ruta/al/archivo}} 5 {*}`

- Inicia una nueva parte cada 5 líneas, ignorando el error de división exacta:

`csplit {{[-k|--keep-files]}} {{ruta/al/archivo}} 5 {*}`

- Divide un archivo a partir de la línea 5 y utiliza un prefijo personalizado para los archivos de salida (el valor por defecto es `xx`):

`csplit {{ruta/al/archivo}} 5 {{[-f|--prefix]}} {{prefijo}}`

- Divide un archivo a partir de la primera línea que coincida con un patrón `regex`:

`csplit {{ruta/al/archivo}} /{{regex}}/`
