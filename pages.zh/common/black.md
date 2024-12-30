# black

> 自动格式化 Python 代码。
> 更多信息：<https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html>。

- 自动格式化一个文件或整个目录：

`black {{path/to/file_or_directory}}`

- 格式化作为字符串传入的 [c]ode：

`black -c "{{code}}"`

- 显示如果格式化文件或目录，将会进行的更改：

`black --check {{path/to/file_or_directory}}`

- 显示对文件或目录将要进行的更改，但不实际执行（干运行）：

`black --diff {{path/to/file_or_directory}}`

- 自动格式化文件或目录，仅将错误消息输出到 `stderr`：

`black --quiet {{path/to/file_or_directory}}`

- 自动格式化文件或目录，而不将单引号替换为双引号（适用于现有项目的帮助工具，避免在新项目中使用）：

`black --skip-string-normalization {{path/to/file_or_directory}}`