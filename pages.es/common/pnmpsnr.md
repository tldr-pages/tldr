# pnmpsnr

> Calcula la diferencia entre dos imágenes.
> Más información: <https://netpbm.sourceforge.net/doc/pnmpsnr.html>.

- Calcula la diferencia, es decir, la relación señal-ruido (PSNR) entre dos imágenes:

`pnmpsnr {{ruta/al/archivo1.pnm}} {{ruta/al/archivo2.pnm}}`

- Compara los componentes de color en lugar de los componentes de luminancia y crominancia de las imágenes:

`pnmpsnr {{ruta/al/archivo1.pnm}} {{ruta/al/archivo2.pnm}} -rgb`

- Ejecuta en modo de comparación, es decir, solo la salida `nomatch` o `match` dependiendo de si el cálculo PSNR supera `n` o no:

`pnmpsnr {{ruta/al/archivo1.pnm}} {{ruta/al/archivo2.pnm}} -target {{n}}`

- Ejecuta en modo comparación y compara los componentes individuales de la imagen, es decir, Y, Cb y Cr, con los umbrales correspondientes:

`pnmpsnr {{ruta/al/archivo1.pnm}} {{ruta/al/archivo2.pnm}} -target1 {{umbral_Y}} -target2 {{umbral_Cb}} -target3 {{umbral_Cr}}`

- Ejecuta en modo comparación y compara los componentes individuales de la imagen, es decir, rojo, verde y azul con los umbrales correspondientes:

`pnmpsnr {{ruta/al/archivo1.pnm}} {{ruta/al/archivo2.pnm}} -rgb -target1 {{umbral_rojo}} -target2 {{umbral_verde}} -target3 {{umbral_azul}}`

- Produce salida legible para máquinas:

`pnmpsnr {{ruta/al/archivo1.pnm}} {{ruta/al/archivo2.pnm}} -machine`
