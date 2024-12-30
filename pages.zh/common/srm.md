# srm

> 安全地删除文件或目录。
> 通过一次或多次覆盖现有数据来实现。是 rm 的替代工具。
> 更多信息：<https://srm.sourceforge.net/srm.html>。

- 以随机数据进行单次覆盖后删除文件：

`srm -s {{path/to/file}}`

- 以随机数据进行七次覆盖后删除文件：

`srm -m {{path/to/file}}`

- 递归删除目录及其内容，使用随机数据对每个文件进行单次覆盖：

`srm -r -s {{path/to/directory}}`

- 在每次删除之前提示确认：

`srm -i {{\*}}`