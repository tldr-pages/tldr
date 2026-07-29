# expand

> 将制表符转换为空格。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/expand-invocation.html>。

- 将每个文件中的制表符转换为空格，写入 `stdout`：

`expand {{路径/到/文件}}`

- 将制表符转换为空格，从 `stdin` 读取：

`expand`

- 不转换非空白字符后的制表符：

`expand {{[-i|--initial]}} {{路径/到/文件}}`

- 设置制表符之间的字符间距，而非默认的 8：

`expand {{[-t|--tabs]}} {{数字}} {{路径/到/文件}}`

- 使用逗号分隔的显式制表符位置列表：

`expand {{[-t|--tabs]}} {{1,4,6}}`
