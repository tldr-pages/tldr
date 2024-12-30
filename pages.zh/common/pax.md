# pax

> 归档和复制工具。
> 更多信息：<https://manned.org/pax.1p>。

- 列出归档的内容：

`pax -f {{archive.tar}}`

- 列出 `gzip` 归档的内容：

`pax -zf {{archive.tar.gz}}`

- 从文件创建归档：

`pax -wf {{target.tar}} {{path/to/file1 path/to/file2 ...}}`

- 从文件创建归档，使用输出重定向：

`pax -w {{path/to/file1 path/to/file2 ...}} > {{target.tar}}`

- 将归档提取到当前目录：

`pax -rf {{source.tar}}`

- 复制到目录，同时保留原始元数据；`target/` 必须存在：

`pax -rw {{path/to/file1}} {{path/to/directory1 path/to/directory2 ...}} {{target/}}`