# ogrmerge.py

> 合并多个矢量数据集为一个。
> 更多信息：<https://gdal.org/programs/ogrmerge.html>.

- 创建一个 GeoPackage，为每个输入的 Shapefile 创建一个图层：

`ogrmerge.py -f {{GPKG}} -o {{path/to/output.gpkg}} {{path/to/input1.shp path/to/input2.shp ...}}`

- 创建一个虚拟数据源（VRT），为每个输入的 GeoJSON 创建一个图层：

`ogrmerge.py -f {{VRT}} -o {{path/to/output.vrt}} {{path/to/input1.geojson path/to/input2.geojson ...}}`

- 将两个矢量数据集合并，并在属性 'source_name' 中存储数据集的源名称：

`ogrmerge.py -single -f {{GeoJSON}} -o {{path/to/output.geojson}} -src_layer_field_name country {{source_name}} {{path/to/input1.shp path/to/input2.shp ...}}`
