# gdal_translate

> Convert raster data between different formats.
> More information: <https://gdal.org/programs/gdal_translate>.

- Convert a raster dataset to JPEG format:

`gdal_translate -of {{JPEG}} {{path/to/input.tif}} {{path/to/output.jpeg}}`

- Assign a projection to a raster dataset:

`gdal_translate -a_srs {{EPSG:4326}} {{path/to/input.tif}} {{path/to/output.tif}}`

- Reduce the size of a raster dataset to a specific fraction:

`gdal_translate -outsize {{40%}} {{40%}} {{path/to/input.tif}} {{path/to/output.tif}}`

- Convert a GeoTiff to a Cloud Optimized GeoTiff:

`gdal_translate {{path/to/input.tif}} {{path/to/output.tif}} -of COG -co COMPRESS=LZW`
