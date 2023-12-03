# ag

> The Silver Searcher. Como `ack`, pero apunta a ser más rápido.
> Más información: <https://github.com/ggreer/the_silver_searcher>.

- Encuentra archivos que contengan "foo", e imprime las líneas coincidentes en su contexto:

`ag {{foo}}`

- Busca archivos que contengan "foo" en un directorio específico:

`ag {{foo}} {{ruta/al/directorio}}`

- Busca archivos que contengan "foo", pero sólo se alistan los nombres de los archivos:

`ag -l {{foo}}`

- Busca archivos que contengan "FOO" sin distinguir entre mayúsculas y minúsculas, e imprime sólo la coincidencia, en lugar de toda la línea:

`ag -i -o {{FOO}}`

- Busca "foo" en archivos cuyo nombre coincide con "bar":

`ag {{foo}} -G {{bar}}`

- Busca archivos cuyo contenido coincide con una expresión regular:

`ag '{{^ba(r|z)$}}'`

- Busca archivos con un nombre que coincida con "foo":

`ag -g {{foo}}`
