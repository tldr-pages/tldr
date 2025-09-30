# pbpaste

> Envía el contenido del portapapeles a la salida estándar.
> Comparable a pulsar `<Cmd v>` en el teclado.
> Más información: <https://keith.github.io/xcode-man-pages/pbcopy.1>.

- Escribe el contenido del portapapeles en un archivo:

`pbpaste > {{ruta/al/archivo}}`

- Utiliza el contenido del portapapeles como entrada de un comando:

`pbpaste | grep foo`
