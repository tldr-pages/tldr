# readelf

> Muestra información sobre archivos ELF.
> Más información: <http://man7.org/linux/man-pages/man1/readelf.1.html>.

- Muestra toda la información sobre el archivo ELF:

`readelf -all {{ruta/al/binario}}`

- Muestra todas las cabeceras presentes en el archivo ELF:

`readelf --headers {{ruta/al/binario}}`

- Muestra las entradas en la sección de la tabla de símbolos del archivo ELF, si tieneff una:

`readelf --symbols {{ruta/al/binario}}`

- Muestra la información de la cabecera ELF:

`readelf --file-header {{ruta/al/binario}}`

- Muestra información de cabecera de la sección ELF:

`readelf --section-headers {{ruta/al/binario}}`
