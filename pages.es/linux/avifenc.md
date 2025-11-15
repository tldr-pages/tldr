# avifenc

> Codificador de formato de archivo de imagen AV1 (AVIF).
> Más información: <https://aomediacodec.github.io/av1-avif/>.

- Convierte una imagen PNG específica a AVIF:

`avifenc {{ruta/a/entrada.png}} {{ruta/a/salida.avif}}`

- Codifica con una velocidad específica (6=predeterminado, 0=el más lento y 10=el más rápido):

`avifenc --speed {{2}} {{ruta/a/entrada.png}} {{ruta/a/salida.avif}}`
