# gdal_translate

> Փոխարկեք պատկերային տվյալները տարբեր ձևաչափերի միջև:.
> Լրացուցիչ տեղեկություններ. <https://gdal.org/en/stable/programs/gdal_translate.html>:.

- Ռաստերային տվյալների հավաքածուն փոխարկեք JPEG ձևաչափի.:

`gdal_translate -of {{JPEG}} {{path/to/input.tif}} {{path/to/output.jpeg}}`

- Նշանակեք պրոյեկցիա ռաստերային տվյալների բազայի վրա.:

`gdal_translate -a_srs {{EPSG:4326}} {{path/to/input.tif}} {{path/to/output.tif}}`

- Կրճատել ռաստերային տվյալների բազայի չափը որոշակի մասի.:

`gdal_translate -outsize {{40%}} {{40%}} {{path/to/input.tif}} {{path/to/output.tif}}`

- Փոխակերպեք GeoTiff-ը ամպի օպտիմիզացված GeoTiff-ի.:

`gdal_translate {{path/to/input.tif}} {{path/to/output.tif}} -of COG -co COMPRESS=LZW`
