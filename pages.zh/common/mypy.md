# mypy

> 检查 Python 代码的类型。
> 更多信息：<https://mypy.readthedocs.io/en/stable/running_mypy.html>。

- 检查特定文件的类型：

`mypy {{path/to/file.py}}`

- 检查特定模块的类型：

`mypy {{[-m|--module]}} {{module_name}}`

- 检查特定包的类型：

`mypy {{[-p|--package]}} {{package_name}}`

- 检查代码字符串的类型：

`mypy {{[-c|--command]}} "{{code}}"`

- 忽略缺失的导入：

`mypy --ignore-missing-imports {{path/to/file_or_directory}}`

- 显示详细的错误信息：

`mypy {{[--tb|--show-traceback]}} {{path/to/file_or_directory}}`

- 指定自定义配置文件：

`mypy --config-file {{path/to/config_file}}`

- 显示帮助信息：

`mypy {{[-h|--help]}}`