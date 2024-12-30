# pycodestyle

> 检查 Python 代码是否符合 PEP 8 风格规范。
> 更多信息：<https://pycodestyle.readthedocs.io>。

- 检查单个文件的风格：

`pycodestyle {{file.py}}`

- 检查多个文件的风格：

`pycodestyle {{file1.py file2.py ...}}`

- 仅显示错误的第一次出现：

`pycodestyle --first {{file.py}}`

- 显示每个错误的源代码：

`pycodestyle --show-source {{file.py}}`

- 显示每个错误的具体 PEP 8 文本：

`pycodestyle --show-pep8 {{file.py}}`