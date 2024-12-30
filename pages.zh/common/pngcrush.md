# pngcrush

> PNG压缩工具。
> 更多信息：<https://pmt.sourceforge.io/pngcrush>。

- 压缩一个PNG文件：

`pngcrush {{in.png}} {{out.png}}`

- 压缩所有PNG文件并将其输出到指定目录：

`pngcrush -d {{path/to/output}} *.png`

- 使用所有114种可用算法压缩PNG文件，并选择最佳结果：

`pngcrush -rem allb -brute -reduce {{in.png}} {{out.png}}`