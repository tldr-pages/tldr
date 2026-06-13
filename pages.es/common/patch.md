# patch

> Emparcha un archivo (o archivos) con un archivo diff.
> Ten en cuenta que los archivos diff deben ser generados por el comando `diff`.
> Más información: <https://manned.org/patch>.

- Aplica un parche usando un archivo diff (los nombres de archivo deben incluirse en el archivo diff):

`patch < {{parche.diff}}`

- Aplica un parche a un archivo específico:

`patch < {{parche.diff}} {{ruta/al/archivo}}`

- Emparcha un archivo escribiendo el resultado a un archivo diferente:

`patch < {{parche.diff}} {{ruta/al/archivo_de_entrada}} {{[-o|--output]}} {{ruta/al/archivo_resultado}}`

- Aplica un parche al directorio actual:

`patch < {{parche.diff}} {{[-p|--strip]}} 1`

- Aplica el reverso de un parche:

`patch < {{parche.diff}} {{[-R|--reverse]}}`
