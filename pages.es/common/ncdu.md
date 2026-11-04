# ncdu

> Analizador de uso de disco con una interfaz ncurses.
> Vea también: `duf`, `df`.
> Más información: <https://dev.yorhel.nl/ncdu/man>.

- Analiza el directorio de trabajo actual:

`ncdu`

- Colorea la salida:

`ncdu --color {{dark|off}}`

- Analiza un directorio específico:

`ncdu {{ruta/al/directorio}}`

- Guarda los resultados en un archivo:

`ncdu -o {{ruta/al/archivo}}`

- Excluye los archivos que coincidan con un patrón (el argumento se puede repetir para añadir más patrones):

`ncdu --exclude '{{*.txt}}'`
