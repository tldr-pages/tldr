# ippeveps

> 打印到 Adobe PostScript 打印机。
> 支持 PDF、PostScript、JPEG、PWG Raster 或 Apple Raster 文件。
> 参见：`ippevepcl`、`ippeveprinter`。
> 更多信息：<https://openprinting.github.io/cups/doc/man-ippevepcl.html>。

- 将文件打印到 `stdout`（状态和进度消息发送到 `stderr`）：

`ippeveps {{path/to/file}}`

- 从 `stdin` 将文件打印到 `stdout`：

`{{wget -O - https://examplewebsite.com/file}} | ippeveps`
