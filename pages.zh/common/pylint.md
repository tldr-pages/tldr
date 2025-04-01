# pylint

> Python 代码检查工具。
> 更多信息：<https://pylint.pycqa.org/en/latest/>.

- 显示文件中的 lint 错误：

`pylint {{path/to/file.py}}`

- 检查一个包或模块（必须可导入；不要添加 `.py` 后缀）：

`pylint {{package_or_module}}`

- 从目录路径检查一个包（必须包含 `__init__.py` 文件）：

`pylint {{path/to/directory}}`

- 检查文件并使用配置文件（通常命名为 `pylintrc`）：

`pylint --rcfile {{path/to/pylintrc}} {{path/to/file.py}}`

- 检查文件并禁用特定错误代码：

`pylint --disable {{C,W,no-error,design}} {{path/to/file}}`
