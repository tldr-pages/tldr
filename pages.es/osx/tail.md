# tail

> Muestra la última parte de un archivo.
> Vea también: `head`.
> Más información: <https://keith.github.io/xcode-man-pages/tail.1.html>.

- Muestra las últimas líneas 'count' del archivo:

`tail -n {{8}} {{ruta/al/archivo}}`

- Imprime un archivo a partir de un número de línea específico:

`tail -n +{{8}} {{ruta/al/archivo}}`

- Imprime un recuento específico de bytes desde el final de un archivo determinado:

`tail -c {{8}} {{ruta/al/archivo}}`

- Imprime las últimas líneas de un archivo dado y sigue leyéndolo hasta `<Ctrl c>`:

`tail -f {{ruta/al/archivo}}`

- Sigue leyendo el archivo hasta `<Ctrl c>`, incluso si el archivo es inaccesible:

`tail -F {{ruta/al/archivo}}`

- Muestra las últimas líneas 'contadas' en 'archivo' y lo actualiza cada 'n' segundos:

`tail -n {{8}} -s {{10}} -f {{ruta/al/archivo}}`
