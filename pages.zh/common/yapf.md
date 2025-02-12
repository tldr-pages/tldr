# yapf

> Python 风格指南检查器。
> 更多信息：<https://github.com/google/yapf>.

- 显示将要进行的更改的差异，但不实际更改（试运行）：

`yapf --diff {{路径/到/文件}}`

- 就地格式化文件，并显示更改的差异：

`yapf --diff --in-place {{路径/到/文件}}`

- 递归格式化目录中的所有 Python 文件，并发执行：

`yapf --recursive --in-place --style {{pep8}} --parallel {{路径/到/目录}}`
