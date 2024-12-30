# gdalbuildvrt

> 从现有数据集列表构建虚拟数据集。
> 更多信息：<https://gdal.org/programs/gdalbuildvrt.html>。

- 从目录中包含的所有 TIFF 文件制作虚拟马赛克：

`gdalbuildvrt {{path/to/output.vrt}} {{path/to/input_directory/*.tif}}`

- 从文本文件中指定名称的文件制作虚拟马赛克：

`gdalbuildvrt -input_file_list {{path/to/list.txt}} {{path/to/output.vrt}}`

- 从 3 个单波段输入文件制作 RGB 虚拟马赛克：

`gdalbuildvrt -separate {{path/to/rgb.vrt}} {{path/to/red.tif}} {{path/to/green.tif}} {{path/to/blue.tif}}`

- 制作具有蓝色背景的虚拟马赛克（RGB：0 0 255）：

`gdalbuildvrt -hidenodata -vrtnodata "{{0 0 255}}" {{path/to/output.vrt}} {{path/to/input_directory/*.tif}}`