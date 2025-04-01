# filefrag

> 报告某个文件的碎片化程度。
> 更多信息：<https://manned.org/filefrag>.

- 显示一个或多个文件的报告：

`filefrag {{path/to/file1 path/to/file2 ...}}`

- 使用 1024 字节块大小显示报告：

`filefrag -k {{path/to/file}}`

- 使用指定的块大小显示报告：

`filefrag -b{{1024|1K|1M|1G|...}} {{path/to/file}}`

- 在请求映射前同步文件：

`filefrag -s {{path/to/file1 path/to/file2 ...}}`

- 显示扩展属性的映射：

`filefrag -x {{path/to/file1 path/to/file2 ...}}`

- 显示包含详细信息的报告：

`filefrag -v {{path/to/file1 path/to/file2 ...}}`