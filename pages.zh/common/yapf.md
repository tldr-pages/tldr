# yapf

> Python 风格指南检查器。
> 更多信息：<https://github.com/google/yapf>。

- 显示将要进行的更改的差异，而不实际进行更改（干运行）：

`yapf --diff {{path/to/file}}`

- 在文件中进行格式化并显示更改的差异：

`yapf --diff --in-place {{path/to/file}}`

- 递归格式化目录中的所有 Python 文件，并行处理：

`yapf --recursive --in-place --style {{pep8}} --parallel {{path/to/directory}}`