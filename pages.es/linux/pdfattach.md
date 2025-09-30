# pdfattach

> Agrega un nuevo archivo adjunto (incorporándolo) a un archivo PDF existente.
> Vea también: `pdfdetach`, `pdfimages`, `pdfinfo`.
> Más información: <https://manned.org/pdfattach>.

- Añade un nuevo adjunto a un archivo PDF existente:

`pdfattach {{ruta/al/archivo_original.pdf}} {{ruta/al/archivo_a_adjuntar}} {{ruta/al/resultado.pdf}}`

- Reemplaza el adjunto del mismo nombre, si existe:

`pdfattach -replace {{ruta/al/archivo_original.pdf}} {{ruta/al/archivo_adjunto}} {{ruta/al/resultado.pdf}}`

- Muestra la ayuda:

`pdfattach -h`

- Muestra la versión:

`pdfattach -v`
