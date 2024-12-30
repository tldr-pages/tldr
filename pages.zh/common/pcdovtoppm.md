# pcdovtoppm

> 根据照片 CD 的概述文件创建索引图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/pcdovtoppm.html>。

- 从 PCD 概述文件创建 PPM 索引图像：

`pcdovtoppm {{path/to/file.pcd}} > {{path/to/output.ppm}}`

- 指定输出图像的[最]大宽度和输出中每个图像的最大[尺]寸：

`pcdovtoppm -m {{width}} -s {{size}} {{path/to/file.pcd}} > {{path/to/output.ppm}}`

- 指定横向最大图像数量[a]和最大[颜]色数量：

`pcdovtoppm -a {{n_images}} -c {{n_colours}} {{path/to/file.pcd}} > {{path/to/output.ppm}}`

- 使用指定的[f]ont 进行注释，并将背景涂成[w]白色：

`pcdovtoppm -f {{font}} -w {{path/to/file.pcd}} > {{path/to/output.ppm}}`