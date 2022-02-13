# gdalinfo

> List various information about a GDAL supported raster dataset..
> More information: <https://gdal.org/programs/gdalinfo.html#gdalinfo>.

- List supported raster formats:

`gdalinfo --formats`

- List information about a raster dataset:

`gdalinfo {{input.tif}}`

- List information about a raster dataset as JSON:

`gdalinfo -json {{input.tif}}`

- Show histogram values of a raster dataset:

`gdalinfo -hist {{input.tif}}`

- List information about a Web Map Service(WMS):

`gdalinfo WMS:{{https://services.meggsimum.de/geoserver/ows}}`

- List information about a specific dataset of a Web Map Service(WMS):

`gdalinfo WMS:{{https://services.meggsimum.de/geoserver/ows}} -sd {{4}}`
