# gdal_translate

> Convert raster data between different formats.
> More information: <https://gdal.org/programs/gdal_translate.html>.

- Convert raster dataset to different format:

`gdal_translate -of {{JPEG}} {{path/to/input.tif}} {{path/to/output.jpeg}}`

- Assign a projection to a raster dataset:

`gdal_translate -a_srs {{EPSG:4326}} {{path/to/input.tif}} {{path/to/output.tif}}`

- Reduce the size of a raster dataset:

`gdal_translate -outsize {{40%}} {{40%}} {{path/to/input.tif}} {{path/to/output.tif}}`

- Convert a GeoTiff to a Cloud Optimzed GeoTiff:

`gdal_translate {{path/to/input.tif}} {{path/to/output.tif}} -of COG -co COMPRESS=LZW`
