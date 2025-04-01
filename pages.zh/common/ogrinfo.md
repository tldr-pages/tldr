# ogrinfo

> 列出有关 OGR 支持的数据源的信息。
> 更多信息：<https://gdal.org/programs/ogrinfo.html>.

- 列出支持的格式：

`ogrinfo --formats`

- 列出数据源的图层：

`ogrinfo {{path/to/input.gpkg}}`

- 获取数据源中特定图层的详细信息：

`ogrinfo {{path/to/input.gpkg}} {{layer_name}}`

- 显示数据源中特定图层的摘要信息：

`ogrinfo -so {{path/to/input.gpkg}} {{layer_name}}`

- 显示数据源中所有图层的摘要：

`ogrinfo -so -al {{path/to/input.gpkg}}`

- 显示符合特定条件的要素的详细信息：

`ogrinfo -where '{{attribute_name > 42}}' {{path/to/input.gpkg}} {{layer_name}}`

- 使用 SQL 更新数据源中的图层：

`ogrinfo {{path/to/input.geojson}} -dialect SQLite -sql "{{UPDATE input SET attribute_name = 'foo'}}"`
