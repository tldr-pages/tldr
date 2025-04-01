# ogr2ogr

> 在不同的文件格式之间转换地理矢量数据。
> 更多信息：<https://gdal.org/programs/ogr2ogr.html>.

- 将 Shapefile 转换为 GeoPackage：

`ogr2ogr -f GPKG {{path/to/output.gpkg}} {{path/to/input.shp}}`

- 根据条件筛选 GeoJSON 中的要素：

`ogr2ogr -where '{{myProperty > 42}}' -f {{GeoJSON}} {{path/to/output.geojson}} {{path/to/input.geojson}}`

- 将 GeoPackage 的坐标参考系统从 `EPSG:4326` 转换为 `EPSG:3857`：

`ogr2ogr -s_srs {{EPSG:4326}} -t_srs {{EPSG:3857}} -f GPKG {{path/to/output.gpkg}} {{path/to/input.gpkg}}`

- 将 CSV 文件转换为 GeoPackage，指定坐标列的名称并分配坐标参考系统：

`ogr2ogr -f GPKG {{path/to/output.gpkg}} {{path/to/input.csv}} -oo X_POSSIBLE_NAMES={{longitude}} -oo Y_POSSIBLE_NAMES={{latitude}} -a_srs {{EPSG:4326}}`

- 将 GeoPackage 加载到 PostGIS 数据库中：

`ogr2ogr -f PostgreSQL PG:dbname="{{database_name}}" {{path/to/input.gpkg}}`

- 将 GeoPackage 文件中的图层裁剪到指定的边界框：

`ogr2ogr -spat {{min_x}} {{min_y}} {{max_x}} {{max_y}} -f GPKG {{path/to/output.gpkg}} {{path/to/input.gpkg}}`