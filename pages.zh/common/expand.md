# expand

> 将制表符转换为空格。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/expand-invocation.html>.

- 将每个文件中的制表符转换为空格，输出到 `stdout`：

`expand {{path/to/file}}`

- 从 `stdin` 读取并转换制表符为空格：

`expand`

- 不转换非空白字符后的制表符：

`expand {{[-i|--initial]}} {{path/to/file}}`

- 设置制表符间隔为指定的字符数，而不是默认的 8：

`expand {{[-t|--tabs]}} {{number}} {{path/to/file}}`

- 使用逗号分隔的显式制表位列表：

`expand {{[-t|--tabs]}} {{1,4,6}}`