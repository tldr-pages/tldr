# tail

> 显示文件的最后一部分。
> 另请参阅：`head`。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/tail-invocation.html>.

- 显示文件中最后 n 行：

`tail --lines {{n}} {{路径/到/文件}}`

- 从特定行号开始打印文件后续内容：

`tail --lines +{{行号}} {{路径/到/文件}}`

- 从给定文件末尾打印特定字节数量的内容：

`tail --bytes {{字节数}} {{路径/到/文件}}`

- 打印给定文件的最后几行并保持读取直到 “Ctrl + C”：

`tail --follow {{路径/到/文件}}`

- 保持读取文件直到 “Ctrl + C”，即使文件无法访问：

`tail --retry --follow {{路径/到/文件}}`

- 显示文件中最后 n 行并每 t 秒刷新一次：

`tail --lines {{n}} --sleep-interval {{t}} --follow {{路径/到/文件}}`
