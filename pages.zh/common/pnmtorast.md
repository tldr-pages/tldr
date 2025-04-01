# pnmtorast

> 将 PNM 文件转换为 Sun 光栅文件。
> 更多信息：<https://netpbm.sourceforge.net/doc/pnmtorast.html>.

- 将 PNM 图像转换为 RAST 图像：

`pnmtorast {{path/to/input.pnm}} > {{path/to/output.rast}}`

- 强制输出为 `RT_STANDARD` 或 `RT_BYTE_ENCODED` 格式：

`pnmtorast -{{standard|rle}} {{path/to/input.pnm}} > {{path/to/output.rast}}`
