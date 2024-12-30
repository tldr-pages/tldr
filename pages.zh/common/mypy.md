# mypy

> 类型检查 Python 代码。
> 更多信息：<https://mypy.readthedocs.io/en/stable/running_mypy.html>。

- 类型检查特定文件：

`mypy {{path/to/file.py}}`

- 类型检查特定 [m]odule：

`mypy -m {{module_name}}`

- 类型检查特定 [p]ackage：

`mypy -p {{package_name}}`

- 类型检查一段代码字符串：

`mypy -c "{{code}}"`

- 忽略缺少的导入：

`mypy --ignore-missing-imports {{path/to/file_or_directory}}`

- 显示详细错误信息：

`mypy --show-traceback {{path/to/file_or_directory}}`

- 指定自定义配置文件：

`mypy --config-file {{path/to/config_file}}`

- 显示 [h]elp：

`mypy -h`