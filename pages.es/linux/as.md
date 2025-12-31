# as

> Ensamblador GNU portátil.
> Principalmente destinado a ensamblar la salida de `gcc` para ser utilizada por `ld`.
> Más información: <https://manned.org/as>.

- Ensambla un archivo, escribiendo la salida en `a.out`:

`as {{ruta/al/archivo.s}}`

- Ensambla la salida en un archivo específico:

`as {{ruta/al/archivo.s}} -o {{ruta/al/archivo_salida.o}}`

- Genera la salida más rápida omitiendo el preprocesamiento de espacios en blanco y comentarios. (Solo debe usarse con compiladores de confianza):

`as -f {{ruta/al/archivo.s}}`

- Incluye una ruta específica en la lista de directorios para buscar archivos especificados en las directivas `.include`:

`as -I {{ruta/al/directorio}} {{ruta/al/archivo.s}}`
