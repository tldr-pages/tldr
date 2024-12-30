# 扩展

> 将制表符转换为空格。
> 更多信息：<https://www.gnu.org/software/coreutils/expand>。

- 将每个文件中的制表符转换为空格，写入 `stdout`：

`expand {{path/to/file}}`

- 从 `stdin` 读取，将制表符转换为空格：

`expand`

- 不在非空白字符后转换制表符：

`expand -i {{path/to/file}}`

- 制表符之间的字符数不是 8，而是某个特定的数字：

`expand -t {{number}} {{path/to/file}}`

- 使用以逗号分隔的显式制表符位置列表：

`expand -t {{1,4,6}}`