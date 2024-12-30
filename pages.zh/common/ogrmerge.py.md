# ogrmerge.py

> 将多个矢量数据集合并为一个。
> 更多信息：<https://gdal.org/programs/ogrmerge.html>。

- 创建一个GeoPackage，每个输入Shapefile对应一个图层：

`ogrmerge.py -f {{GPKG}} -o {{path/to/output.gpkg}} {{path/to/input1.shp path/to/input2.shp ...}}`

- 创建一个虚拟数据源（VRT），每个输入GeoJSON对应一个图层：

`ogrmerge.py -f {{VRT}} -o {{path/to/output.vrt}} {{path/to/input1.geojson path/to/input2.geojson ...}}`

- 连接两个矢量数据集，并将数据集的源名称存储在属性'source_name'中：

`ogrmerge.py -single -f {{GeoJSON}} -o {{path/to/output.geojson}} -src_layer_field_name country {{source_name}} {{path/to/input1.shp path/to/input2.shp ...}}`