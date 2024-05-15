# a2ping

> Convierte imágenes en archivos EPS o PDF.
> Más información: <https://manned.org/a2ping>.

- Convierte una imagen a PDF (Nota: Especificar un nombre de archivo de salida es opcional):

`a2ping {{ruta/al/imagen.ext}} {{ruta/al/salida.pdf}}`

- Comprime el documento utilizando el método especificado:

`a2ping --nocompress {{none|zip|best|flate}} {{ruta/al/archivo}}`

- Escanea HiResBoundingBox si está presente (Nota: por defecto es sí):

`a2ping --nohires {{ruta/al/archivo}}`

- Permite el contenido de la página por debajo y a la izquierda del origen (Nota: por defecto es no):

`a2ping --below {{ruta/al/archivo}}`

- Pasa argumentos adicionales a `gs`:

`a2ping --gsextra {{argumentos}} {{ruta/al/archivo}}`

- Pasa argumentos adicionales a un programa externo (por ejemplo, `pdftops`):

`a2ping --extra {{argumentos}} {{ruta/al/archivo}}`

- Muestra ayuda:

`a2ping -h`
