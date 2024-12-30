# cat

> 打印和连接文件。
> 更多信息：<https://keith.github.io/xcode-man-pages/cat.1.html>。

- 将文件的内容打印到 `stdout`：

`cat {{path/to/file}}`

- 将多个文件连接成一个输出文件：

`cat {{path/to/file1 path/to/file2 ...}} > {{path/to/output_file}}`

- 将多个文件追加到输出文件：

`cat {{path/to/file1 path/to/file2 ...}} >> {{path/to/output_file}}`

- 将文件的内容复制到输出文件，不进行缓冲：

`cat -u {{/dev/tty12}} > {{/dev/tty13}}`

- 将 `stdin` 写入文件：

`cat - > {{path/to/file}}`

- 为所有输出行编号：

`cat -n {{path/to/file}}`

- 显示不可打印和空白字符（如果是非ASCII字符则带有 `M-` 前缀）：

`cat -v -t -e {{path/to/file}}`