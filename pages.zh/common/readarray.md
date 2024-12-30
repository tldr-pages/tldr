# readarray

> 从 `stdin` 读取行到数组中。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-readarray>。

- 交互式输入行到数组中：

`readarray {{array_name}}`

- 从文件读取行并插入到数组中：

`readarray {{array_name}} < {{path/to/file.txt}}`

- 移除尾随的分隔符（默认为换行符）：

`readarray -t {{array_name}} < {{path/to/file.txt}}`

- 最多复制指定数量的行：

`readarray -n {{N}} {{array_name}} < {{path/to/file.txt}}`