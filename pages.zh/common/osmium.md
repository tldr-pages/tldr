# osmium

> 多用途工具，用于处理开放街道地图 (OSM) 文件。
> 更多信息：<https://osmcode.org/osmium-tool/manual>.

- 显示文件信息：

`osmium fileinfo {{path/to/input.osm}}`

- 显示内容：

`osmium show {{path/to/input.osm}}`

- 将文件格式从 PBF 转换为 XML：

`osmium cat {{path/to/input.osm.pbf}} {{[-o|--output]}} {{path/to/output.osm}}`

- 根据给定的 [b]ounding box 提取地理区域：

`osmium extract {{[-b|--bbox]}} {{min_longitude}},{{min_latitude}},{{max_longitude}},{{max_latitude}} {{path/to/input.pbf}} {{[-o|--output]}} {{path/to/output.pbf}}`

- 根据 GeoJSON 文件提取地理区域：

`osmium extract {{[-p|--polygon]}} {{path/to/polygon.geojson}} {{path/to/input.pbf}} {{[-o|--output]}} {{path/to/output.pbf}}`

- 过滤所有标记为 "restaurant" 的对象：

`osmium tags-filter {{path/to/input.pbf}} amenity=restaurant {{[-o|--output]}} {{path/to/output.pbf}}`

- 过滤标记为 "highway" 的 "way" 对象：

`osmium tags-filter {{path/to/input.pbf}} w/highway {{[-o|--output]}} {{path/to/output.pbf}}`

- 过滤标记为 "building" 的 "way" 和 "relation" 对象：

`osmium tags-filter {{path/to/input.pbf}} wr/building {{[-o|--output]}} {{path/to/output.pbf}}`