# pamundice

> Combina una cuadrícula de imágenes Netpbm en una sola.
> Vea también: `pamdice`.
> Más información: <https://netpbm.sourceforge.net/doc/pamundice.html>.

- Combina las imágenes cuyos nombres coincidan con la expresión de nombre de archivo al estilo `printf`. Supongamos una cuadrícula con un tamaño específico:

`pamundice {{nombrearchivo_%1d_%1a.ppm}} {{[-a|-across]}} {{grid_width}} {{[-d|-down]}} {{grid_height}} > {{ruta/a/salida.ppm}}`

- Supongamos que los mosaicos se solapan horizontal y verticalmente en la cantidad especificada:

`pamundice {{nombrearchivo_%1d_%1a.ppm}} {{[-a|-across]}} {{valor_x}} {{[-d|-down]}} {{valor_y}} {{[-ho|-hoverlap]}} {{valor}} {{[-vo|-voverlap]}} {{valor}} > {{ruta/a/salida.ppm}}`

- Especifica las imágenes que se van a combinar mediante un archivo de texto que contenga un nombre de archivo por línea:

`pamundice {{[-l|-listfile]}} {{ruta/a/archivo.txt}} {{[-a|-across]}} {{valor_x}} {{[-d|-down]}} {{valor_y}} > {{ruta/a/salida.ppm}}`
