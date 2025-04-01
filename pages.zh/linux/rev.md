# rev

> 反转文本行或文件的内容。
> 更多信息：<https://manned.org/rev>。

- 反转在终端中输入的文本：

`rev`

- 反转文本字符串 "hello"：

`echo "hello" | rev`

- 反转整个文件并输出到 `stdout`：

`rev {{path/to/file}}`

- 使用 '\0' 作为行分隔符（零终止）：

`rev {{[-0|--zero]}} {{path/to/file}}`

- 显示帮助信息：

`rev {{[-h|--help]}}`

- 显示版本信息：

`rev {{[-V|--version]}}`
