# gdaldem

> Tool to analyze and visualize DEM (digital elevation models).
> More information: <https://gdal.org/programs/gdaldem.html>.

- Create a hillshade from a DEM:

`gdaldem hillshade {{path/to/input.tif}} {{path/to/output.tif}}`

- Compute the slope of a DEM:

`gdaldem slope {{input.tif}} {{output.tif}}`

- Compute the aspect of a DEM:

`gdaldem aspect {{input.tif}} {{output.tif}}`
