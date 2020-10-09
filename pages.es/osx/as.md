# as

> Ensamblador portable GNU.
> Principalmente destinado a ensamblar la salida de `gcc` para ser utilizada por` ld`.

- Ensamblar un archivo, escribiendo la salida en a.out:

`as {{file.s}}`

- Ensamblar la salida de un archivo dado:

`as {{file.s}} -o {{out.o}}`

- Genera resultados más rápido omitiendo los espacios en blanco y el preprocesamiento de comentarios. (Solo debe usarse para compiladores de confianza):

`as -f {{file.s}}`

- Incluye una ruta determinada a la lista de directorios para buscar archivos especificados en las directivas .include:

`as -I {{path/to/directory}} {{file.s}}`
