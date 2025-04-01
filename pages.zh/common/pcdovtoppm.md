# pcdovtoppm

> 从 Photo CD 的概述文件创建索引图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/pcdovtoppm.html>.

- 从 PCD 概述文件创建 PPM 索引图像：

`pcdovtoppm {{path/to/file.pcd}} > {{path/to/output.ppm}}`

- 指定输出图像的最大宽度和输出中每个图像的最大尺寸：

`pcdovtoppm {{[-m|-maxwidth]}} {{width}} {{[-s|-size]}} {{size}} {{path/to/file.pcd}} > {{path/to/output.ppm}}`

- 指定输出图像中每行的最大图像数量和最大颜色数：

`pcdovtoppm {{[-a|-across]}} {{n_images}} {{[-c|-colors]}} {{n_colours}} {{path/to/file.pcd}} > {{path/to/output.ppm}}`

- 使用指定的字体进行注释并绘制白色背景：

`pcdovtoppm {{[-f|-font]}} {{font}} {{[-w|-white]}} {{path/to/file.pcd}} > {{path/to/output.ppm}}`
