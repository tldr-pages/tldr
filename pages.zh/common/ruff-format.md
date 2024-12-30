# ruff 格式

> 一个极其快速的 Python 代码格式化工具。
> 如果没有指定文件或目录，默认使用当前工作目录。
> 更多信息请访问：<https://docs.astral.sh/ruff/formatter>。

- 在原地格式化指定的文件或目录：

`ruff format {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 打印哪些文件将被修改，如果有文件需要重新格式化，则返回非零退出码，否则返回零：

`ruff format --check`

- 打印将会做出哪些更改，而不修改文件：

`ruff format --diff`