# tail

> 显示文件的最后部分。
> 另见：`head`。
> 更多信息：<https://www.gnu.org/software/coreutils/tail>。

- 显示文件中的最后 'count' 行：

`tail --lines {{count}} {{path/to/file}}`

- 从特定行号开始打印文件：

`tail --lines +{{count}} {{path/to/file}}`

- 从给定文件的末尾打印特定字节数：

`tail --bytes {{count}} {{path/to/file}}`

- 打印给定文件的最后几行，并持续读取直到按下 `Ctrl + C`：

`tail --follow {{path/to/file}}`

- 持续读取文件直到按下 `Ctrl + C`，即使文件无法访问：

`tail --retry --follow {{path/to/file}}`

- 显示 'file' 中的最后 'num' 行，并每 'n' 秒刷新一次：

`tail --lines {{count}} --sleep-interval {{seconds}} --follow {{path/to/file}}`