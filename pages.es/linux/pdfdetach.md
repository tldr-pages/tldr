# pdfdetach

> Lista o extrae archivos adjuntos (archivos embebidos) de un archivo PDF.
> Vea también: `pdfattach`, `pdfimages`, `pdfinfo`.
> Más información: <https://manned.org/pdfdetach>.

- Lista todos los archivos adjuntos en un archivo con una codificación de texto específica:

`pdfdetach list -enc {{UTF-8}} {{ruta/al/archivo.pdf}}`

- Guarda un archivo embebido especificado por su número:

`pdfdetach -save {{número}} {{ruta/a/la/entrada.pdf}}`

- Guarda un archivo embebido especificando su nombre:

`pdfdetach -savefile {{nombre}} {{ruta/al/archivo.pdf}}`

- Guarda el archivo embebido con un nombre de archivo de salida personalizado:

`pdfdetach -save {{número}} -o {{ruta/al/resultado}} {{ruta/a/la/entrada.pdf}}`

- Guarda el adjunto desde un archivo protegido por contraseña del propietario/usuario:

`pdfdetach -save {{número}} {{-opw|-upw}} {{contraseña}} {{ruta/a/la/entrada.pdf}}`
