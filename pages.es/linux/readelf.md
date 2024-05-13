# readelf

> Muestra información sobre archivos ELF.
> Más información: <https://manned.org/readelf.1>.

- Muestra toda la información de un archivo ELF:

`readelf -all {{ruta/al/archivo_binario}}`

- Muestra todas las cabeceras presentes en un archivo ELF:

`readelf --headers {{ruta/al/archivo_binario}}`

- Muestra las entradas en la sección de la tabla de símbolos del archivo ELF, si tiene una:

`readelf --symbols {{ruta/al/archivo_binario}}`

- Muestra la información de la cabecera ELF:

`readelf --file-header {{ruta/al/archivo_binario}}`

- Muestra información de cabecera de la sección ELF:

`readelf --section-headers {{ruta/al/archivo_binario}}`
