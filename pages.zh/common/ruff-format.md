# ruff format

> 一个极其快速的 Python 代码格式化工具。
> 如果没有指定文件或目录，则默认使用当前工作目录。
> 更多信息：<https://docs.astral.sh/ruff/formatter>.

- 格式化指定的文件或目录：

`ruff format {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 打印哪些文件将被修改，如果有文件需要重新格式化则返回非零退出代码，否则返回零：

`ruff format --check`

- 打印将要进行的更改而不修改文件：

`ruff format --diff`
