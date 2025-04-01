# gdalinfo

> 列出 GDAL 支持的栅格数据集的各种信息。
> 更多信息：<https://gdal.org/programs/gdalinfo.html>。

- 列出所有支持的栅格格式：

`gdalinfo --formats`

- 列出特定栅格数据集的信息：

`gdalinfo {{path/to/input.tif}}`

- 以 JSON 格式列出特定栅格数据集的信息：

`gdalinfo -json {{path/to/input.tif}}`

- 显示特定栅格数据集的直方图值：

`gdalinfo -hist {{path/to/input.tif}}`

- 列出 Web 地图服务 (WMS) 的信息：

`gdalinfo WMS:{{https://services.meggsimum.de/geoserver/ows}}`

- 列出 Web 地图服务 (WMS) 中特定数据集的信息：

`gdalinfo WMS:{{https://services.meggsimum.de/geoserver/ows}} -sd {{4}}`
