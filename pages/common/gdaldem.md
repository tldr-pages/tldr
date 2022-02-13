# gdaldem

> Tool to analyze and visualize digital elevation models(DEM).
> More information: <https://gdal.org/programs/gdaldem.html>.

- Create a hillshade from a DEM:

`gdaldem hillshade {{input.tif}} {{output.tif}}`

- Compute the slope of a DEM:

`gdaldem slope {{input.tif}} {{output.tif}}`

- Compute the aspect of a DEM:

`gdaldem aspect {{input.tif}} {{output.tif}}`
