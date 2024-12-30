# csplit

> 将文件拆分成多个部分。
> 这会生成名为 "xx00"、"xx01" 等的文件。
> 更多信息：<https://www.gnu.org/software/coreutils/csplit>。

- 在第 5 行和第 23 行拆分文件：

`csplit {{path/to/file}} 5 23`

- 每 5 行拆分一次文件（如果总行数不能被 5 整除，则会失败）：

`csplit {{path/to/file}} 5 {*}`

- 每 5 行拆分一次文件，忽略整除错误：

`csplit -k {{path/to/file}} 5 {*}`

- 在第 5 行拆分文件，并为输出文件使用自定义前缀：

`csplit {{path/to/file}} 5 -f {{prefix}}`

- 在匹配正则表达式的行处拆分文件：

`csplit {{path/to/file}} /{{regular_expression}}/`