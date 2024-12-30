# gdal_contour

> 从数字高程模型创建等高线和多边形。
> 更多信息: <https://gdal.org/programs/gdal_contour.html>。

- 创建一个矢量数据集，包含间隔为100米的等高线，并将高程属性命名为“ele”：

`gdal_contour -a {{ele}} -i {{100.0}} {{path/to/input.tif}} {{path/to/output.gpkg}}`

- 创建一个矢量数据集，包含间隔为100米的多边形：

`gdal_contour -i {{100.0}} -p {{path/to/input.tif}} {{path/to/output.gpkg}}`