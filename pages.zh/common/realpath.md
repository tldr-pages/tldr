# realpath

> 显示文件或目录的解析绝对路径。
> 更多信息：<https://www.gnu.org/software/coreutils/realpath>。

- 显示文件或目录的绝对路径：

`realpath {{path/to/file_or_directory}}`

- 要求所有路径组件必须存在：

`realpath --canonicalize-existing {{path/to/file_or_directory}}`

- 在符号链接之前解析“..”组件：

`realpath --logical {{path/to/file_or_directory}}`

- 禁用符号链接扩展：

`realpath --no-symlinks {{path/to/file_or_directory}}`

- 抑制错误信息：

`realpath --quiet {{path/to/file_or_directory}}`