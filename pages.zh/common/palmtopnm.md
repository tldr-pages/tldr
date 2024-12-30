# palmtopnm

> 将 Palm 位图文件转换为 PNM 图像。
> 更多信息：<https://netpbm.sourceforge.net/doc/palmtopnm.html>。

- 将 Palm 位图转换为 PNM 图像：

`palmtopnm {{path/to/file.palm}} > {{path/to/file.pnm}}`

- 显示输入文件的信息：

`palmtopnm -verbose {{path/to/file.palm}} > {{path/to/file.pnm}}`

- 转换输入文件中包含的图像的第 n 个版本：

`palmtopnm -rendition {{n}} {{path/to/file.palm}} > {{path/to/file.pnm}}`

- 将输入文件中颜色的直方图写入 `stdout`：

`palmtopnm -showhist {{path/to/file.palm}} > {{path/to/file.pnm}}`

- 如果设置了，输出输入图像的透明颜色：

`palmtopnm -transparent {{path/to/file.palm}}`