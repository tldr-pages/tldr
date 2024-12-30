# ippeveps

> 打印到Adobe PostScript打印机。
> 支持PDF、PostScript、JPEG、PWG Raster或Apple Raster文件。
> 另请参见: `ippevepcl`, `ippeveprinter`。
> 更多信息: <https://openprinting.github.io/cups/doc/man-ippevepcl.html>。

- 将文件打印到`stdout`（状态和进度消息发送到`stderr`）：

`ippeveps {{path/to/file}}`

- 从`stdin`打印文件到`stdout`：

`{{wget -O - https://examplewebsite.com/file}} | ippeveps`