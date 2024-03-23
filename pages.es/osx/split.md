# split

> Divide un archivo en trozos.
> Más información: <https://keith.github.io/xcode-man-pages/split.1.html>.

- Divide un archivo, cada división tiene 10 líneas (excepto la última división):

`split -l {{10}} {{nombre_de_archivo}}`

- Divide un fichero mediante una expresión regular. La línea que coincida será la primera línea del siguiente archivo de salida:

`split -p {{cat|^[dh]og}} {{nombre_de_archivo}}`

- Divide un archivo con 512 bytes en cada división (excepto en la última; utiliza 512k para kilobytes y 512m para megabytes):

`split -b {{512}} {{nombre_de_archivo}}`

- Divide un archivo en 5 archivos. El archivo se divide de forma que cada división tenga el mismo tamaño (excepto la última división):

`split -n {{5}} {{nombre_de_archivo}}`
