# autopep8

> 根据 PEP 8 风格指南格式化 Python 代码。
> 更多信息：<https://github.com/hhatto/autopep8>.

- 将文件格式化并输出到 `stdout`，并自定义最大行长度：

`autopep8 {{路径/到/文件.py}} --max-line-length {{长度}}`

- 格式化文件，并显示更改的差异：

`autopep8 --diff {{路径/到/文件}}`

- 就地格式化文件并保存更改：

`autopep8 --in-place {{路径/到/文件.py}}`

- 递归地就地格式化目录中的所有文件并保存更改：

`autopep8 --in-place --recursive {{路径/到/目录}}`
