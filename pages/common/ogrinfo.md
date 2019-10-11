# ogrinfo

> List information about an OGR-supported data source.
> More information: <https://gdal.org/programs/ogrinfo.html>.

- List layers of a GeoPackage:

`ogrinfo {{input.gpkg}}`

- Get detailed information about a specific layer:

`ogrinfo {{input.gpkg}} {{layer_name}}`

- Only show summary information about a specific layer:

`ogrinfo -so {{input.gpkg}} {{layer_name}}`
