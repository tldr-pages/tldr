# stdbuf

> 以修改的标准流缓冲操作运行命令。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/stdbuf-invocation.html>.

- 将 `stdin` 缓冲区大小更改为 512 KiB：

`stdbuf {{[-i|--input]}} 512K {{command}}`

- 将 `stdout` 缓冲区更改为行缓冲：

`stdbuf {{[-o|--output]}} L {{command}}`

- 将 `stderr` 缓冲区更改为无缓冲：

`stdbuf {{[-e|--error]}} 0 {{command}}`