# datashader_cli

> 基于 datashader 的命令行工具，用于大数据集的快速可视化。
> 更多信息：<https://github.com/wybert/datashader-cli>.

- 创建一个点的阴影散点图并保存为 PNG 文件，并设置背景颜色：

`datashader_cli points {{path/to/input.parquet}} --x {{pickup_x}} --y {{pickup_y}} {{path/to/output.png}} --background {{black|white|#rrggbb}}`

- 可视化地理空间数据（支持 Geoparquet、shapefile、geojson、geopackage 等）：

`datashader_cli points {{path/to/input_data.geo.parquet}} {{path/to/output_data.png}} --geo true`

- 使用 matplotlib 渲染图像：

`datashader_cli points {{path/to/input_data.geo.parquet}} {{path/to/output_data.png}} --geo {{true}} --matplotlib true`