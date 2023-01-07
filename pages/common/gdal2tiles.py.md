# gdal2tiles.py

> Generate TMS or XYZ tiles for a raster dataset.
> More information: <https://gdal.org/programs/gdal2tiles.html>.

- Generate TMS tiles for the zoom levels 2-5 of a raster dataset:

`gdal2tiles.py --zoom={{2-5}} {{path/to/input.tif}} {{path/to/output_directory}}`

- Generate XYZ tiles for the zoom levels 2-5 of a raster dataset:

`gdal2tiles.py --zoom={{2-5}} --xyz {{path/to/input.tif}} {{path/to/output_directory}}`
