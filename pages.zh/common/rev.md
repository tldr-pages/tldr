# rev

> 反转一行文本或文件。
> 更多信息：<https://manned.org/rev>。

- 反转输入到终端的文本：

`rev`

- 反转文本字符串 "hello"：

`echo "hello" | rev`

- 反转整个文件并打印到 `stdout`：

`rev {{path/to/file}}`

- 使用 '\0' 作为行分隔符（零终止）：

`rev -0 {{path/to/file}}`

- 显示帮助信息：

`rev -h`

- 显示版本信息：

`rev -V`