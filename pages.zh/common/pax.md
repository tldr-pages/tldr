# pax

> 存档和复制工具。
> 更多信息：<https://manned.org/pax.1p>。

- 列出存档中的内容：

`pax -f {{archive.tar}}`

- 列出 `gzip` 压缩存档中的内容：

`pax -zf {{archive.tar.gz}}`

- 从文件创建存档：

`pax -wf {{target.tar}} {{path/to/file1 path/to/file2 ...}}`

- 从文件创建存档，使用输出重定向：

`pax -w {{path/to/file1 path/to/file2 ...}} > {{target.tar}}`

- 将存档解压到当前目录：

`pax -rf {{source.tar}}`

- 复制文件到目录，保留原始元数据；目标目录 `target/` 必须存在：

`pax -rw {{path/to/file1}} {{path/to/directory1 path/to/directory2 ...}} {{target/}}`