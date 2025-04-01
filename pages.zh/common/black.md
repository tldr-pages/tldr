# black

> 自动格式化 Python 代码。
> 更多信息：<https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html>.

- 自动格式化文件或整个目录：

`black {{path/to/file_or_directory}}`

- 格式化作为字符串传递的代码：

`black {{[-c|--code]}} "{{code}}"`

- 显示如果对文件或目录进行格式化是否会对其进行更改：

`black --check {{path/to/file_or_directory}}`

- 显示对文件或目录将要进行的更改但不实际执行（干运行）：

`black --diff {{path/to/file_or_directory}}`

- 自动格式化文件或目录，仅将错误消息输出到 `stderr`：

`black {{[-q|--quiet]}} {{path/to/file_or_directory}}`

- 自动格式化文件或目录，不将单引号替换为双引号（适应助手，新项目中避免使用此选项）：

`black {{[-S|--skip-string-normalization]}} {{path/to/file_or_directory}}`