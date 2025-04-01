# pyflakes

> 检查 Python 源代码文件中的错误。
> 更多信息：<https://pypi.org/project/pyflakes>.

- 检查单个 Python 文件：

`pyflakes check {{path/to/file.py}}`

- 检查特定目录中的 Python 文件：

`pyflakes checkPath {{path/to/directory}}`

- 递归检查目录中的 Python 文件：

`pyflakes checkRecursive {{path/to/directory}}`

- 检查多个目录中找到的所有 Python 文件：

`pyflakes iterSourceCode {{path/to/directory_1}} {{path/to/directory_2}}`