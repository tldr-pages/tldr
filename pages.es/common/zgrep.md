# zgrep

> Busca patrones de texto en archivos contenidos dentro de archivos comprimidos.
> Más información: <https://manned.org/zgrep>.

- Busca un patrón en un archivo comprimido (distingue entre mayúsculas y minúsculas):

`zgrep {{patrón}} {{ruta/al/archivo_comprimido}}`

- Muestra 3 líneas de [C]ontexto alrededor, [B]efore o [A]fter de cada coincidencia:

`zgrep {{--context|--before-context|--after-context}} 3 {{patrón}} {{ruta/al/archivo_comprimido}}`

- Busca un patrón en un archivo comprimido (sin distinguir mayúsculas y minúsculas):

`zgrep {{[-i|--ignore-case]}} {{patrón}} {{ruta/al/archivo_comprimido}}`

- Muestra el recuento de líneas que contienen el patrón coincidente en un archivo comprimido:

`zgrep {{[-c|--count]}} {{patrón}} {{ruta/al/archivo_comprimido}}`

- Muestra las líneas que no contienen el patrón (invertir la función de búsqueda):

`zgrep {{[-v|--invert-match]}} {{patrón}} {{ruta/al/archivo_comprimido}}`

- Busca varios patrones en un archivo comprimido:

`zgrep {{[-e|--regexp]}} "{{patrón_1}}" {{[-e|--regexp]}} "{{patrón_2}}" {{ruta/al/archivo_comprimido}}`

- Usa expresiones regulares extendidas (admite `?`, `+`, `{}`, `()` y `|`):

`zgrep {{[-E|--extended-regexp]}} {{regex}} {{ruta/al/archivo}}`
