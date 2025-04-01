# pngcrush

> PNG 压缩工具。
> 更多信息：<https://pmt.sourceforge.io/pngcrush>。

- 压缩一个 PNG 文件：

`pngcrush {{in.png}} {{out.png}}`

- 压缩所有 PNG 文件，并将它们输出到指定目录：

`pngcrush -d {{path/to/output}} *.png`

- 使用所有 114 种可用算法压缩 PNG 文件，并选择最佳结果：

`pngcrush -rem allb -brute -reduce {{in.png}} {{out.png}}`
