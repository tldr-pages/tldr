# pcdovtoppm

> Crea una imagen índice para un CD de fotos basándose en su archivo de resumen.
> Más información: <https://netpbm.sourceforge.net/doc/pcdovtoppm.html>.

- Crea una imagen índice PPM a partir de un archivo de vista general PCD:

`pcdovtoppm {{ruta/al/archivo.pcd}} > {{ruta/al/archivo.ppm}}`

- Especifica la anchura máxima de la imagen de salida y el tamaño máximo de cada una de las imágenes contenidas en la salida:

`pcdovtoppm {{[-m|-maxwidth]}} {{anchura}} {{[-s|-size]}} {{tamaño}} {{ruta/al/archivo.pcd}} > {{ruta/al/archivo.ppm}}`

- Especifica el número máximo de imágenes y el número máximo de colores:

`pcdovtoppm {{[-a|-across]}} {{n_imágenes}} {{[-c|-colors]}} {{n_colores}} {{ruta/al/archivo.pcd}} > {{ruta/al/archivo_salida.ppm}}`

- Utiliza la fuente especificada para las anotaciones y pinta el fondo blanco:

`pcdovtoppm {{[-f|-font]}} {{fuente}} {{[-w|-white]}} {{ruta/al/archivo.pcd}} > {{ruta/al/archivo.ppm}}`
