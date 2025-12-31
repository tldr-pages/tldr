# pamcut

> Corta una región rectangular de una imagen Netpbm.
> Vea también: `pamcrop`, `pamdice`, `pamcomp`.
> Más información: <https://netpbm.sourceforge.net/doc/pamcut.html>.

- Descarta la cantidad de columnas/filas especificadas a cada lado de la imagen:

`pamcut {{[-cropl|-cropleft]}} {{valor}} {{[-cropr|-cropright]}} {{valor}} {{[-cropt|-croptop]}} {{valor}} {{[-cropb|-cropbottom]}} {{valor}} {{ruta/a/la/imagen.ppm}} > {{ruta/al/resultado.ppm}}`

- Mantiene solo las columnas entre las columnas especificadas (inclusivamente):

`pamcut {{[-l|-left]}} {{valor}} {{[-ri|-right]}} {{valor}} {{ruta/a/la/imagen.ppm}} > {{ruta/al/resultado.ppm}}`

- Llena áreas perdidas con píxeles negros si el rectángulo especificado no se encuentra completamente dentro de la imagen de entrada:

`pamcut {{[-t|-top]}} {{valor}} {{[-b|-bottom]}} {{valor}} -pad {{ruta/a/la/imagen.ppm}} > {{ruta/al/resultado.ppm}}`
