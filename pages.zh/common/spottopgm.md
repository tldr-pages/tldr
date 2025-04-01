# spottopgm

> 将 SPOT 卫星图像转换为 PGM 格式。
> 更多信息：<https://netpbm.sourceforge.net/doc/spottopgm.html>。

- 将指定的 SPOT 图像转换为 PGM 格式：

`spottopgm {{path/to/file.spot}} > {{path/to/output.pgm}}`

- 提取指定的颜色通道：

`spottopgm -{{1|2|3}} {{path/to/file.spot}} > {{path/to/output.pgm}}`

- 从输入图像中提取指定的矩形区域：

`spottopgm {{first_col first_row last_col last_row}} {{path/to/file.spot}} > {{path/to/output.pgm}}`
