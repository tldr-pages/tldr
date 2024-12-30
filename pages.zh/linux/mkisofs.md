# mkisofs

> 从目录创建 ISO 文件。
> 也可以用别名 `genisoimage`。
> 更多信息：<https://manned.org/mkisofs>。

- 从目录创建 ISO：

`mkisofs -o {{filename.iso}} {{path/to/source_directory}}`

- 在创建 ISO 时设置光盘标签：

`mkisofs -o {{filename.iso}} -V "{{label_name}}" {{path/to/source_directory}}`