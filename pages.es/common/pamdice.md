# pamdice

> Divide una imagen Netpbm en secciones verticales u horizontales.
> Vea también: `pamundice`.
> Más información: <https://netpbm.sourceforge.net/doc/pamdice.html>.

- Divide una imagen Netpbm de modo que los mosaicos resultantes tengan la altura y la anchura especificadas:

`pamdice {{[-o|-outstem]}} {{ruta/a/nombre_archivo_stem}} {{[-he|-height]}} {{valor}} {{[-w|-width]}} {{valor}} {{ruta/a/entrada.ppm}}`

- Hace que las piezas resultantes se superpongan en la cantidad especificada tanto horizontal como verticalmente:

`pamdice {{[-o|-outstem]}} {{ruta/a/nombre_archivo_stem}} {{[-he|-height]}} {{valor}} {{[-w|-width]}} {{valor}} {{[-ho|-hoverlap]}} {{valor}} {{[-vo|-voverlap]}} {{valor}} {{ruta/a/input.ppm}}`
