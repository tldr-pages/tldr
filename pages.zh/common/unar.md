# unar

> 从归档文件中提取内容。
> 更多信息：<https://manned.org/unar>。

- 将归档提取到当前目录：

`unar {{path/to/archive}}`

- 将归档提取到指定目录：

`unar -o {{path/to/directory}} {{path/to/archive}}`

- 如果要解压的文件已存在，则强制覆盖：

`unar -f {{path/to/archive}}`

- 如果要解压的文件已存在，则强制重命名：

`unar -r {{path/to/archive}}`

- 如果要解压的文件已存在，则强制跳过：

`unar -s {{path/to/archive}}`