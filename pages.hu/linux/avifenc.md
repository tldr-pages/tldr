# avifenc

> AV1 Image File Format (AVIF) kódoló. További információ: <https://aomediacodec.github.io/av1-avif/>.

- Egy adott PNG kép átalakítása AVIF formátumba:

`avifenc {{path/to/image.png}} {{path/to/image.avif}}`

- Kódolás egy adott sebességgel, ahol 0=leglassabb, 10=leggyorsabb és 6=alapértelmezett:

`avifenc --speed {{2}} {{path/to/image.png}} {{path/to/image.avif}}`
