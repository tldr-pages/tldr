# autopep8

> 根据 PEP 8 风格指南格式化 Python 代码。
> 更多信息：<https://github.com/hhatto/autopep8>。

- 将文件格式化为 `stdout`，并使用自定义的最大行长度：

`autopep8 {{path/to/file.py}} --max-line-length {{length}}`

- 格式化文件，并显示更改的 diff：

`autopep8 --diff {{path/to/file}}`

- 在原地格式化文件并保存更改：

`autopep8 --in-place {{path/to/file.py}}`

- 递归地格式化目录中的所有文件，并在原地保存更改：

`autopep8 --in-place --recursive {{path/to/directory}}`
