# pnmtosgi

> 将 PNM 文件转换为 SGI 图像文件。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmtosgi.html>.

- 将 PNM 图像转换为 SGI 图像：

`pnmtosgi {{path/to/input.pnm}} > {{path/to/output.sgi}}`

- 禁用或启用压缩：

`pnmtosgi -{{verbatim|rle}} {{path/to/input.pnm}} > {{path/to/output.sgi}}`

- 将指定的字符串写入 SGI 图像头的 `imagename` 字段：

`pnmtosgi -imagename {{string}} {{path/to/input.pnm}} > {{path/to/output.sgi}}`
