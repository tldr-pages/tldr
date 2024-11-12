# eu-readelf

> Muestra información sobre archivos ELF.
> Más información: <https://manned.org/eu-readelf>.

- Muestra toda la información extraíble en un archivo ELF:

`eu-readelf --all {{ruta/al/archivo}}`

- Muestra el contenido de todos los segmentos y secciones de NOTE, o de un segmento o sección en particular:

`eu-readelf --notes[={{.note.ABI-tag}}] {{ruta/al/fichero}}`
