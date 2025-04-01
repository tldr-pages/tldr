# tail

> 显示文件的最后一部分。
> 参见：`head`。
> 更多信息：<https://keith.github.io/xcode-man-pages/tail.1.html>。

- 显示文件的最后 'count' 行：

`tail -n {{8}} {{path/to/file}}`

- 从特定行号开始打印文件：

`tail -n +{{8}} {{path/to/file}}`

- 从给定文件的末尾打印特定数量的字节：

`tail -c {{8}} {{path/to/file}}`

- 打印给定文件的最后几行，并持续读取直到 `<Ctrl c>`：

`tail -f {{path/to/file}}`

- 即使文件不可访问，也持续读取文件直到 `<Ctrl c>`：

`tail -F {{path/to/file}}`

- 显示 'file' 的最后 'count' 行，并每 'seconds' 秒刷新一次：

`tail -n {{8}} -s {{10}} -f {{path/to/file}}`
