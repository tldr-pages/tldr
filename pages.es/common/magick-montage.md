# magick montage

> Coloca imágenes en una cuadrícula personalizable.
> Ver también: `magick`.
> Más información: <https://imagemagick.org/script/montage.php>.

- Colocar imágenes en una cuadrícula, redimensionando automáticamente las imágenes más grandes que el tamaño de la celda de la cuadrícula:

`magick montage {{ruta/a/imagen1.jpg ruta/a/imagen2.jpg ...}} {{ruta/a/montaje.jpg}}`

- Colocar imágenes en una cuadrícula, calculando automáticamente el tamaño de la celda de la cuadrícula a partir de la imagen más grande:

`magick montage {{ruta/a/imagen1.jpg ruta/a/imagen2.jpg ...}} -geometry {{+0+0}} {{ruta/a/montaje.jpg}}`

- Especificar el tamaño de la celda de la cuadrícula y redimensionar las imágenes para ajustarlas antes de colocarlas en la cuadrícula:

`magick montage {{ruta/a/imagen1.jpg ruta/a/imagen2.jpg ...}} -geometry {{640x480+0+0}} {{ruta/a/montaje.jpg}}`

- Limitar el número de filas y columnas en la cuadrícula, causando que las imágenes de entrada desborden en múltiples montajes de salida:

`magick montage {{ruta/a/imagen1.jpg ruta/a/imagen2.jpg ...}} -geometry {{+0+0}} -tile {{2x3}} {{montaje_%d.jpg}}`

- Redimensionar y recortar las imágenes para llenar sus celdas de cuadrícula antes de colocarlas:

`magick montage {{ruta/a/imagen1.jpg ruta/a/imagen2.jpg ...}} -geometry {{+0+0}} -resize {{640x480^}} -gravity {{center}} -crop {{640x480+0+0}} {{ruta/a/montaje.jpg}}`
