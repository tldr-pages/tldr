# gdalinfo

> List various information about a GDAL supported raster dataset.
> More information: <https://gdal.org/programs/gdalinfo.html>.

- List supported raster formats:

`gdalinfo --formats`

- List information about a raster dataset:

`gdalinfo {{path/to/input.tif}}`

- List information about a raster dataset in JSON format:

`gdalinfo -json {{path/to/input.tif}}`

- Show histogram values of a raster dataset:

`gdalinfo -hist {{path/to/input.tif}}`

- List information about a Web Map Service (WMS):

`gdalinfo WMS:{{https://services.meggsimum.de/geoserver/ows}}`

- List information about a specific dataset of a Web Map Service (WMS):

`gdalinfo WMS:{{https://services.meggsimum.de/geoserver/ows}} -sd {{4}}`
