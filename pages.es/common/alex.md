# alex

> Una herramienta que detecta escritura insensible y desconsiderada.
> Ayuda a encontrar en el texto frases que son parciales con el género, que polarizan, o están relacionadas con la raza, son desconsideradas con la religión u otras frases tendenciosas.
> Más información: <https://github.com/get-alex/alex>.

- Analiza texto desde `stdin`:

`echo {{His network looks good}} | alex --stdin`

- Analiza todos los archivos del directorio actual:

`alex`

- Analiza un archivo dado:

`alex {{ruta/al/archivo_de_texto.md}}`

- Analiza todos los archivos Markdown excepto `ejemplo.md`.:

`alex *.md !{{ruta/hacia/ejemplo.md}}`
