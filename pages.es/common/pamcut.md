# pamcut

> Corta una región rectangular de una imagen Netpbm.
> Vea también: `pamcrop`, `pamdice`, `pamcomp`.
> Más información: <https://netpbm.sourceforge.net/doc/pamcut.html>.

- Descarta la cantidad de columnas/filas especificadas a cada lado de la imagen:

`pamcut -cropleft {{valor}} -cropright {{valor}} -croptop {{valor}} -cropbottom {{valor}} {{ruta/a/la/imagen.ppm}} > {{ruta/al/resultado.ppm}}`

- Mantiene solo las columnas entre las columnas especificadas (inclusivamente):

`pamcut -left {{valor}} -right {{valor}} {{ruta/a/la/imagen.ppm}} > {{ruta/al/resultado.ppm}}`

- Llena áreas perdidas con píxeles negros si el rectángulo especificado no se encuentra completamente dentro de la imagen de entrada:

`pamcut -top {{valor}} -bottom {{valor}} -pad {{ruta/a/la/imagen.ppm}} > {{ruta/al/resultado.ppm}}`
