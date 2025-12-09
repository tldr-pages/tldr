# patch

> Emparcha un archivo (o archivos) con un archivo diff.
> Ten en cuenta que los archivos diff deben ser generados por el comando `diff`.
> Más información: <https://manned.org/patch>.

- Aplica un parche usando un archivo diff (los nombres de archivo deben incluirse en el archivo diff):

`patch < {{parche.diff}}`

- Aplica un parche a un archivo específico:

`patch {{ruta/al/archivo}} < {{parche.diff}}`

- Emparcha un archivo escribiendo el resultado a un archivo diferente:

`patch {{ruta/al/archivo_de_entrada}} -o {{ruta/al/archivo_resultado}} < {{parche.diff}}`

- Aplica un parche al directorio actual:

`patch -p1 < {{parche.diff}}`

- Aplica el reverso de un parche:

`patch -R < {{parche.diff}}`
