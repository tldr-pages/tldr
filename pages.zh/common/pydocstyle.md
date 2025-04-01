# pydocstyle

> 静态检查 Python 脚本是否符合 Python 文档字符串约定。
> 更多信息：<https://www.pydocstyle.org/en/latest/>.

- 分析 Python 脚本或特定目录中的所有 Python 脚本：

`pydocstyle {{file.py|path/to/directory}}`

- 显示每个错误的解释：

`pydocstyle {{[-e|--explain]}} {{file.py|path/to/directory}}`

- 显示调试信息：

`pydocstyle {{[-d|--debug]}} {{file.py|path/to/directory}}`

- 显示错误总数：

`pydocstyle --count {{file.py|path/to/directory}}`

- 使用特定的配置文件：

`pydocstyle --config {{path/to/config_file}} {{file.py|path/to/directory}}`

- 忽略一个或多个错误：

`pydocstyle --ignore {{D101,D2,D107,...}} {{file.py|path/to/directory}}`

- 检查特定约定中的错误：

`pydocstyle --convention {{pep257|numpy|google}} {{file.py|path/to/directory}}`
