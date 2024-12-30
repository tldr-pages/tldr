# gdaldem

> 分析和可视化数字高程模型（DEM）。
> 更多信息：<https://gdal.org/programs/gdaldem.html>。

- 计算 DEM 的阴影效果：

`gdaldem hillshade {{path/to/input.tif}} {{path/to/output.tif}}`

- 计算 DEM 的坡度：

`gdaldem slope {{path/to/input.tif}} {{path/to/output.tif}}`

- 计算 DEM 的方位：

`gdaldem aspect {{path/to/input.tif}} {{path/to/output.tif}}`