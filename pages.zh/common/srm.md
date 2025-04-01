# srm

> 安全地删除文件或目录。
> 通过一次或多次覆盖现有数据来删除。是 rm 的替代工具。
> 更多信息：<https://srm.sourceforge.net/srm.html>.

- 使用随机数据覆盖一次后删除文件：

`srm -s {{path/to/file}}`

- 使用随机数据覆盖七次后删除文件：

`srm -m {{path/to/file}}`

- 使用随机数据覆盖一次后递归删除目录及其内容：

`srm -r -s {{path/to/directory}}`

- 在每次删除前提示确认：

`srm -i {{\*}}`
