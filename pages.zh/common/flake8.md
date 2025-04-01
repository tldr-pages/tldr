# flake8

> 检查 Python 代码的风格和质量。
> 更多信息：<https://flake8.pycqa.org/>。

- 递归地检查文件或目录：

`flake8 {{path/to/file_or_directory}}`

- 递归地检查文件或目录，并显示每个错误出现的行：

`flake8 --show-source {{path/to/file_or_directory}}`

- 递归地检查文件或目录，并忽略一系列规则。（所有可用规则可在 flake8rules.com 查看）：

`flake8 --ignore {{rule1,rule2}} {{path/to/file_or_directory}}`

- 递归地检查文件或目录，但排除匹配给定通配符或子字符串的文件：

`flake8 --exclude {{substring1,glob2}} {{path/to/file_or_directory}}`