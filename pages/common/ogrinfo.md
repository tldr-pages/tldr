# ogrinfo

> List information about an OGR-supported data source.
> More information: <https://gdal.org/programs/ogrinfo.html>.

- List supported formats:

`ogrinfo --formats`

- List layers of a data source:

`ogrinfo {{path/to/input.gpkg}}`

- Get detailed information about a specific layer of a data source:

`ogrinfo {{path/to/input.gpkg}} {{layer_name}}`

- Show summary information about a specific layer of a data source:

`ogrinfo -so {{path/to/input.gpkg}} {{layer_name}}`

- Show summary of all layers of the data source:

`ogrinfo -so -al {{path/to/input.gpkg}}`

- Show detailed information of features matching a condition:

`ogrinfo -where '{{attribute_name > 42}}' {{path/to/input.gpkg}} {{layer_name}}`

- Update a layer in the data source with SQL:

`ogrinfo {{path/to/input.geojson}} -dialect SQLite -sql "{{UPDATE input SET attribute_name = 'foo'}}"`
