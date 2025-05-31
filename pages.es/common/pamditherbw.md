# pamditherbw

> Aplica dithering a una imagen en escala de grises, es decir, la convierte en un patrón de píxeles blancos y negros que parecen iguales a la escala de grises original.
> Vea también: `pbmreduce`.
> Más información: <https://netpbm.sourceforge.net/doc/pamditherbw.html>.

- Lee una imagen PGM, aplica la separación y la guarda en un archivo:

`ppmditherbw {{ruta/a/la/imagen.pgm}} > {{ruta/al/archivo.pgm}}`

- Utiliza el método de cuantización especificado:

`ppmditherbw -{{floyd|fs|atkinson|threshold|hilbert|...}} {{ruta/a/la/imagen.pgm}} > {{ruta/al/archivo.pgm}}`

- Utiliza el método de cuantización de atkinson y la semilla especificada para un generador de número pseudo-aleatorio:

`ppmditherbw {{[-a|-atkinson]}} {{[-r|-randomseed]}} {{1337}} {{ruta/a/la/imagen.pgm}} > {{ruta/al/archivo.pgm}}`

- Especifica el valor de umbralización (thresholding) para los métodos de cuantización que realizan algún tipo de umbralización:

`ppmditherbw -{{fs|atkinson|thresholding}} {{[-va|-value]}} {{0.3}} {{ruta/a/la/imagen.pgm}} > {{ruta/al/archivo.pgm}}`
