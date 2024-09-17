# as

> Ensamblador portable GNU.
> Principalmente destinado a ensamblar la salida de `gcc` para ser utilizada por` ld`.
> Más información: <https://keith.github.io/xcode-man-pages/as.1.html>.

- Ensambla un archivo, escribiendo la salida en `a.out`:

`as {{ruta/al/archivo.s}}`

- Ensambla la salida a un archivo especificado:

`as {{ruta/al/archivo.s}} -o {{salida.o}}`

- Genera resultados más rápidos omitiendo los espacios en blanco y el preprocesamiento de comentarios. (Solo debe usarse para compiladores de confianza):

`as -f {{ruta/al/archivo.s}}`

- Incluye una ruta determinada a la lista de directorios para buscar archivos especificados en las directivas `.include`:

`as -I {{ruta/al/directorio}} {{ruta/al/archivo.s}}`
