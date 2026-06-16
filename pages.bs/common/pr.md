# pr

> Paginación o disposición en columnas de archivos para su impresión.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/pr-invocation.html>.

- Imprime varios archivos con un encabezado y un pie de página predeterminados:

`pr {{ruta/al/archivo1 ruta/al/archivo2 ...}}`

- Imprime con un encabezado centrado personalizado:

`pr {{[-h|--header]}} "{{encabezado}}" {{ruta/al/archivo1 ruta/al/archivo2 ...}}`

- Imprime con líneas numeradas y un formato de fecha personalizado:

`pr {{[-n|--number-lines]}} {{[-D|--date-format]}} "{{formato}}" {{ruta/al/archivo1 ruta/al/archivo2 ...}}`

- Imprime todos los archivos juntos, uno en cada columna, sin encabezado ni pie de página:

`pr {{[-m|--merge]}} {{[-T|--omit-pagination]}} {{ruta/al/archivo1 ruta/al/archivo2 ...}}`

- Imprime, comenzando en la página 2 hasta la página 5, con una longitud de página determinada (incluidos el encabezado y el pie de página):

`pr +2:5 {{[-l|--length]}} {{longitud_página}} {{ruta/al/archivo1 ruta/al/archivo2 ...}}`

- Imprime con un sangrado para cada línea y un ancho de página personalizado truncado:

`pr {{[-o|--indent]}} {{sangrado}} {{[-W|--page_width]}} {{ancho}} {{ruta/al/archivo1 ruta/al/archivo2 ...}}`
