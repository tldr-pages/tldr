# ag

> El Buscador de Plata. Como `ack`, pero aspira a ser más rápido.
> Más información: <https://manned.org/ag>.

- Encuentra archivos que contengan «foo», e imprime las líneas coincidentes en contexto:

`ag foo`

- Encuentra archivos que contengan "foo" en un directorio específico:

`ag foo {{ruta/al/directorio}}`

- Encuentra archivos que contengan "foo", pero solo lista los nombres de archivo:

`ag {{[-l|--files-with-matches]}} foo`

- Encuentra archivos que contengan "FOO" sin distinción entre mayúsculas y minúsculas, e imprime solo la coincidencia, en lugar de la línea completa:

`ag {{[-i|--ignore-case]}} {{[-o|--only-matching]}} FOO`

- Busca "foo" en archivos cuyo nombre coincida con "bar":

`ag foo {{[-G|--file-search-regex]}} bar`

- Busca archivos cuyo contenido coincida con una expresión regular:

`ag '{{^ba(r|z)$}}'`

- Busca archivos cuyo nombre coincida con "foo":

`ag {{[-g|--filename-pattern]}} foo`
