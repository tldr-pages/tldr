# tee

> 从 `stdin` 读取内容并写入 `stdout` 和文件（或命令）。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/tee-invocation.html>.

- 将 `stdin` 复制到每个文件，并同时输出到 `stdout`：

`echo "example" | tee {{path/to/file}}`

- 将内容追加到指定文件，不覆盖原有内容：

`echo "example" | tee {{[-a|--append]}} {{path/to/file}}`

- 将 `stdin` 输出到终端，并同时将其传递给另一个程序进行进一步处理：

`echo "example" | tee {{/dev/tty}} | {{xargs printf "[%s]"}}`

- 创建一个名为 "example" 的目录，统计 "example" 中的字符数，并将 "example" 输出到终端：

`echo "example" | tee >(xargs mkdir) >(wc -c)`
