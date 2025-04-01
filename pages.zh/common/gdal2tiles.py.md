# gdal2tiles.py

> 为栅格数据集生成 TMS 或 XYZ 瓦片。
> 更多信息：<https://gdal.org/programs/gdal2tiles.html>。

- 为栅格数据集的 2 到 5 级缩放生成 TMS 瓦片：

`gdal2tiles.py --zoom 2-5 {{path/to/input.tif}} {{path/to/output_directory}}`

- 为栅格数据集的 2 到 5 级缩放生成 XYZ 瓦片：

`gdal2tiles.py --zoom 2-5 --xyz {{path/to/input.tif}} {{path/to/output_directory}}`