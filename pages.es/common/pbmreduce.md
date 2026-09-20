# pbmreduce

> Reduce proporcionalmente una imagen PBM.
> Vea también: `pamenlarge`, `pamditherbw`.
> Más información: <https://netpbm.sourceforge.net/doc/pbmreduce.html>.

- Reduce la imagen especificada en el factor indicado:

`pbmreduce {{n}} {{ruta/a/imagen.pbm}} > {{ruta/a/salida.pbm}}`

- Utiliza un umbral simple al reducir:

`pbmreduce {{[-t|-threshold]}} {{n}} {{ruta/a/imagen.pbm}} > {{ruta/a/salida.pbm}}`

- Utiliza el umbral especificado para todas las cuantificaciones:

`pbmreduce {{[-va|-value]}} {{0.6}} {{n}} {{ruta/a/imagen.pbm}} > {{ruta/a/salida.pbm}}`
