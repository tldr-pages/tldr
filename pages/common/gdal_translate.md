# gdal_translate

> Convert raster data between different formats.
> More information: <https://gdal.org/programs/gdal_translate.html>.

- Convert raster dataset to different format:

`gdal_translate -of {{"JPEG"}} {{world.tif}} {{output.jpeg}}`

- Assign a projection to a raster dataset:

`gdal_translate -a_srs {{EPSG:4326}} {{input.tif}} {{output.tif}}`

- Reduce the size of a raster dataaset:

`gdal_translate -outsize {{40%}} {{40%}} {{elevation.tif}} {{small.tif}}`

- Convert a GeoTiff to a Cloud Optimzed GeoTiff.

`gdal_translate {{input.tif}} {{output.tif}} -of COG -co COMPRESS=LZW`
