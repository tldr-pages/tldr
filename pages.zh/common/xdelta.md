# xdelta

> 差分编码工具。
> 通常用于对二进制文件应用补丁。
> 更多信息：<https://github.com/jmacd/xdelta>。

- 应用补丁：

`xdelta -d -s {{输入文件路径}} {{差分文件路径.xdelta}} {{输出文件路径}}`

- 创建补丁：

`xdelta -e -s {{旧文件路径}} {{新文件路径}} {{输出文件路径.xdelta}}`