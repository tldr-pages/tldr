# pamcut

> 从 Netpbm 图像中裁剪出一个矩形区域。
> 参见：`pamcrop`，`pamdice`，`pamcomp`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pamcut.html>。

- 在图像的每一侧丢弃指定数量的列/行：

`pamcut -cropleft {{值}} -cropright {{值}} -croptop {{值}} -cropbottom {{值}} {{path/to/image.ppm}} > {{path/to/output.ppm}}`

- 仅保留指定列之间的列（包括在内）：

`pamcut -left {{值}} -right {{值}} {{path/to/image.ppm}} > {{path/to/output.ppm}}`

- 如果指定的矩形不完全位于输入图像内，则用黑色像素填充缺失区域：

`pamcut -top {{值}} -bottom {{值}} -pad {{path/to/image.ppm}} > {{path/to/output.ppm}}`