# optipng

> PNG 文件优化工具。
> 更多信息：<https://optipng.sourceforge.net>。

- 使用默认设置压缩 PNG 文件：

`optipng {{path/to/file.png}}`

- 使用最佳压缩比压缩 PNG 文件：

`optipng -o{{7}} {{path/to/file.png}}`

- 使用最快压缩比压缩 PNG 文件：

`optipng -o{{0}} {{path/to/file.png}}`

- 压缩 PNG 文件并添加交错：

`optipng -i {{1}} {{path/to/file.png}}`

- 压缩 PNG 文件并保留所有元数据（包括文件时间戳）：

`optipng -preserve {{path/to/file.png}}`

- 压缩 PNG 文件并删除所有元数据：

`optipng -strip all {{path/to/file.png}}`
