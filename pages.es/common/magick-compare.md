# magick compare

> Crea una imagen de comparación para anotar visualmente la diferencia entre dos imágenes.
> Vea también: `magick`.
> Más información: <https://imagemagick.org/script/compare.php>.

- Compara dos imágenes:

`magick compare {{ruta/a/imagen1.png}} {{ruta/a/imagen2.png}} {{ruta/a/diff.png}}`

- Compara dos imágenes usando una métrica específica:

`magick compare -verbose -metric {{PSNR}} {{ruta/a/imagen1.png}} {{ruta/a/imagen2.png}} {{ruta/a/diff.png}}`
