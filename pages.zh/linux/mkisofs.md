# mkisofs

> 从目录创建 ISO 文件。
> 也别名为 `genisoimage`。
> 更多信息：<https://manned.org/mkisofs>。

- 从目录创建 ISO 文件：

`mkisofs -o {{filename.iso}} {{path/to/source_directory}}`

- 创建 ISO 文件时设置光盘标签：

`mkisofs -o {{filename.iso}} -V "{{label_name}}" {{path/to/source_directory}}`