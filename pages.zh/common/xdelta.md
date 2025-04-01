# xdelta

> 差分编码工具。
> 常用于对二进制文件应用补丁。
> 更多信息：<https://github.com/jmacd/xdelta>。

- 应用补丁：

`xdelta -d -s {{path/to/input_file}} {{path/to/delta_file.xdelta}} {{path/to/output_file}}`

- 创建补丁：

`xdelta -e -s {{path/to/old_file}} {{path/to/new_file}} {{path/to/output_file.xdelta}}`
