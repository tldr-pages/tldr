# lsar

> 列出一个归档文件的内容。
> 另请参见：`unar`，`ar`。
> 更多信息：<https://manned.org/lsar>。

- 列出归档文件的内容：

`lsar {{path/to/archive}}`

- 列出密码保护的归档文件的内容：

`lsar {{path/to/archive}} --password {{password}}`

- 打印归档中每个文件的所有可用信息（非常长）：

`lsar {{-L|--verylong}} {{path/to/archive}}`

- 测试归档中文件的完整性（如果可能）：

`lsar --test {{path/to/archive}}`

- 以 JSON 格式列出归档文件的内容：

`lsar --json {{path/to/archive}}`

- 显示帮助：

`lsar --help`