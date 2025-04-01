# gdalwarp

> 图像重新投影和变形工具。
> 更多信息：<https://gdal.org/programs/gdalwarp.html>。

- 重新投影栅格数据集：

`gdalwarp -t_srs {{EPSG:4326}} {{path/to/input.tif}} {{path/to/output.tif}}`

- 使用特定坐标裁剪栅格数据集：

`gdalwarp -te {{min_x}} {{min_y}} {{max_x}} {{max_y}} -te_srs {{EPSG:4326}} {{path/to/input.tif}} {{path/to/output.tif}}`

- 使用矢量图层裁剪栅格数据集：

`gdalwarp -cutline {{path/to/area_to_cut.geojson}} -crop_to_cutline {{path/to/input.tif}} {{path/to/output.tif}}`
