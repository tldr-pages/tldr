# tee

> 从 `stdin` 读取并写入 `stdout` 和文件（或命令）。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/tee-invocation.html>。

- 将 `stdin` 复制到每个文件，同时也输出到 `stdout`：

`echo "示例" | tee {{路径/到/文件}}`

- 追加到给定文件，不覆盖：

`echo "示例" | tee {{[-a|--append]}} {{路径/到/文件}}`

- 将 `stdin` 输出到终端，同时通过管道传递给另一个程序进行进一步处理：

`echo "示例" | tee {{/dev/tty}} | {{xargs printf "[%s]"}}`

- 创建一个名为 "example" 的目录，统计 "example" 中的字符数，并将 "example" 输出到终端：

`echo "示例" | tee >(xargs mkdir) >(wc {{[-c|--bytes]}})`
