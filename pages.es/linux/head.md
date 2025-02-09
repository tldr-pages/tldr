# head

> Muestra la primera parte de los archivos.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/head-invocation.html>.

- Muestra las primeras líneas de un archivo:

`head --lines {{cuenta}} {{ruta/al/archivo}}`

- Muestra los primeros bits de un archivo:

`head --bytes {{cuenta}} {{ruta/al/archivo}}`

- Muestra todo el contenido de un archivo excepto las últimas líneas:

`head --lines -{{cuenta}} {{ruta/al/archivo}}`

- Muestra todo el contenido de un archivo excepto los últimos bits:

`head --bytes -{{cuenta}} {{ruta/al/archivo}}`
