# gdal_translate

> 将栅格数据转换为不同的格式。
> 更多信息：<https://gdal.org/programs/gdal_translate.html>.

- 将栅格数据集转换为 JPEG 格式：

`gdal_translate -of {{JPEG}} {{path/to/input.tif}} {{path/to/output.jpeg}}`

- 为栅格数据集指定投影：

`gdal_translate -a_srs {{EPSG:4326}} {{path/to/input.tif}} {{path/to/output.tif}}`

- 将栅格数据集的大小缩减为特定的比例：

`gdal_translate -outsize {{40%}} {{40%}} {{path/to/input.tif}} {{path/to/output.tif}}`

- 将 GeoTiff 转换为优化的 GeoTiff：

`gdal_translate {{path/to/input.tif}} {{path/to/output.tif}} -of COG -co COMPRESS=LZW`
