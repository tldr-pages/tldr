# pamcut

> 从 Netpbm 图像中裁剪出一个矩形区域。
> 请参阅：`pamcrop`, `pamdice`, `pamcomp`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pamcut.html>。

- 从图像的每一侧丢弃指定数量的列/行：

`pamcut -cropleft {{value}} -cropright {{value}} -croptop {{value}} -cropbottom {{value}} {{path/to/image.ppm}} > {{path/to/output.ppm}}`

- 仅保留指定列之间的列（包括边界列）：

`pamcut -left {{value}} -right {{value}} {{path/to/image.ppm}} > {{path/to/output.ppm}}`

- 如果指定的矩形区域未完全位于输入图像内，则用黑色像素填充缺失区域：

`pamcut -top {{value}} -bottom {{value}} -pad {{path/to/image.ppm}} > {{path/to/output.ppm}}`