# csplit

> 将文件分割成多个部分。
> 生成的文件将命名为 "xx00", "xx01" 等。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/csplit-invocation.html>。

- 在第 5 行和第 23 行分割文件：

`csplit {{path/to/file}} 5 23`

- 每 5 行分割一次文件（如果总行数不是 5 的倍数，将失败）：

`csplit {{path/to/file}} 5 {*}`

- 每 5 行分割一次文件，忽略精确分割错误：

`csplit {{[-k|--keep-files]}} {{path/to/file}} 5 {*}`

- 在第 5 行分割文件，并为输出文件使用自定义前缀：

`csplit {{path/to/file}} 5 {{[-f|--prefix]}} {{prefix}}`

- 在匹配正则表达式的行处分割文件：

`csplit {{path/to/file}} /{{regular_expression}}/`
