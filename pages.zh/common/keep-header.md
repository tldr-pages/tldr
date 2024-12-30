# 保持头部

> 通过命令保持第一行不变，直接传递给 `stdout`。
> 更多信息：<https://github.com/eBay/tsv-utils#keep-header>。

- 对文件进行排序，保持第一行在顶部：

`keep-header {{path/to/file}} -- sort`

- 直接将第一行输出到 `stdout`，将文件的其余部分传递给指定的命令：

`keep-header {{path/to/file}} -- {{command}}`

- 从 `stdin` 读取，排序除第一行外的所有行：

`cat {{path/to/file}} | keep-header -- {{command}}`

- 对文件进行 grep，保持第一行不受搜索模式的影响：

`keep-header {{path/to/file}} -- grep {{pattern}}`