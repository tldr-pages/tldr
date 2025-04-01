# gdalbuildvrt

> 从现有数据集中构建虚拟数据集。
> 更多信息：<https://gdal.org/programs/gdalbuildvrt.html>。

- 从目录中的所有 TIFF 文件创建虚拟马赛克：

`gdalbuildvrt {{path/to/output.vrt}} {{path/to/input_directory/*.tif}}`

- 从指定在文本文件中的文件名创建虚拟马赛克：

`gdalbuildvrt -input_file_list {{path/to/list.txt}} {{path/to/output.vrt}}`

- 从3个单波段输入文件创建RGB虚拟马赛克：

`gdalbuildvrt -separate {{path/to/rgb.vrt}} {{path/to/red.tif}} {{path/to/green.tif}} {{path/to/blue.tif}}`

- 创建具有蓝色背景（RGB: 0 0 255）的虚拟马赛克：

`gdalbuildvrt -hidenodata -vrtnodata "{{0 0 255}}" {{path/to/output.vrt}} {{path/to/input_directory/*.tif}}`