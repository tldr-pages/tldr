# osmium

> 用于处理 OpenStreetMap (OSM) 文件的多功能工具。
> 更多信息请访问: <https://osmcode.org/osmium-tool/manual>。

- 显示文件信息：

`osmium fileinfo {{path/to/input.osm}}`

- 显示内容：

`osmium show {{path/to/input.osm}}`

- 将文件格式从 PBF 转换为 XML：

`osmium cat {{path/to/input.osm.pbf}} -o {{path/to/output.osm}}`

- 按给定的 [b] 边界框提取地理区域：

`osmium extract -b {{min_longitude}},{{min_latitude}},{{max_longitude}},{{max_latitude}} {{path/to/input.pbf}} -o {{path/to/output.pbf}}`

- 按 GeoJSON 文件提取地理区域：

`osmium extract -p {{path/to/polygon.geojson}} {{path/to/input.pbf}} -o {{path/to/output.pbf}}`

- 过滤所有标记为“餐厅”的对象：

`osmium tags-filter {{path/to/input.pbf}} amenity=restaurant -o {{path/to/output.pbf}}`

- 过滤标记为“公路”的“路径”对象：

`osmium tags-filter {{path/to/input.pbf}} w/highway -o {{path/to/output.pbf}}`

- 过滤标记为“建筑”的“路径”和“关系”对象：

`osmium tags-filter {{path/to/input.pbf}} wr/building -o {{path/to/output.pbf}}`