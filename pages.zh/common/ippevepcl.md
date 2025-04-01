# ippevepcl

> 打印到 HP 黑白 PCL 激光打印机。
> 支持 HP PCL、PWG Raster 和 Apple Raster 文件。
> 请参阅：`ippevepcl`, `ippeveprinter`。
> 更多信息：<https://openprinting.github.io/cups/doc/man-ippevepcl.html>。

- 将文件打印到 `stdout`（状态和进度消息发送到 `stderr`）：

`ippeveps {{path/to/file}}`

- 从 `stdin` 打印文件到 `stdout`：

`{{wget -O - https://examplewebsite.com/file}} | ippeveps`
