# ogrinfo

> Lists information about an OGR-supported data source.
> More information: <https://gdal.org/programs/ogrinfo.html>.

- List layers of a GeoPackage:

`ogrinfo input.gpkg`

- Detailed information about layer:

`ogrinfo input.gpkg layer_42`

- Show summary of layer:

`ogrinfo -so input.gpkg layer_42`
