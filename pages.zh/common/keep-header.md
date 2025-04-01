# keep-header

> 保持命令处理后文件的第一行不变，直接传递给 `stdout`。
> 更多信息：<https://github.com/eBay/tsv-utils#keep-header>。

- 对文件进行排序并保持第一行在顶部：

`keep-header {{path/to/file}} -- sort`

- 直接将第一行输出到 `stdout`，将文件的其余部分传递给指定的命令：

`keep-header {{path/to/file}} -- {{command}}`

- 从 `stdin` 读取，对除第一行以外的所有行进行排序：

`cat {{path/to/file}} | keep-header -- {{command}}`

- 搜索文件，无论搜索模式如何都保留第一行：

`keep-header {{path/to/file}} -- grep {{pattern}}`
