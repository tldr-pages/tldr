# tee

> 从 `stdin` 读取并写入到 `stdout` 和文件（或命令）。
> 更多信息：<https://www.gnu.org/software/coreutils/tee>.

- 将 `stdin` 复制到每个文件，并同时写入 `stdout`：

`echo "example" | tee {{path/to/file}}`

- 追加到给定的文件，而不覆盖：

`echo "example" | tee -a {{path/to/file}}`

- 将 `stdin` 打印到终端，同时将其传递给另一个程序以进行进一步处理：

`echo "example" | tee {{/dev/tty}} | {{xargs printf "[%s]"}}`

- 创建一个名为 "example" 的目录，计算 "example" 中的字符数量，并将 "example" 写入终端：

`echo "example" | tee >(xargs mkdir) >(wc -c)`