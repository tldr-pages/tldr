# lsar

> 列出归档文件的内容。
> 参见：`unar`, `ar`。
> 更多信息：<https://manned.org/lsar>。

- 列出归档文件的内容：

`lsar {{path/to/archive}}`

- 列出受密码保护的归档文件的内容：

`lsar {{path/to/archive}} {{[-p|--password]}} {{password}}`

- 打印归档文件中每个文件的所有可用信息（信息很长）：

`lsar {{[-L|--verylong]}} {{path/to/archive}}`

- 检测归档文件中文件的完整性（如果可能的话）：

`lsar {{[-t|--test]}} {{path/to/archive}}`

- 以 JSON 格式列出归档文件的内容：

`lsar {{[-j|--json]}} {{path/to/archive}}`

- 显示帮助信息：

`lsar {{-h|--help}}`
