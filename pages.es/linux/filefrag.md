# filefrag

> Informa del grado de fragmentación de un archivo en particular.
> Más información: <https://manned.org/filefrag>.

- Muestra un informe para uno o más archivos:

`filefrag {{ruta/al/archivo1 ruta/al/archivo2 ...}}`

- Muestra un informe con un tamaño de bloque de 1024 bytes:

`filefrag -k {{ruta/al/archivo}}`

- Muestra un informe con un tamaño de bloque determinado:

`filefrag -b{{1024|1K|1M|1G|...}} {{ruta/al/archivo}}`

- Sincroniza el archivo antes de solicitar la asignación:

`filefrag -s {{ruta/al/archivo1 ruta/al/archivo2 ...}}`

- Muestra la asignación de atributos extendidos:

`filefrag -x {{ruta/al/archivo1 ruta/al/archivo2 ...}}`

- Muestra un informe con información detallada:

`filefrag -v {{ruta/al/archivo1 ruta/al/archivo2 ...}}`
