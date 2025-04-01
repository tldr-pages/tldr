# cat

> 打印和连接文件。
> 更多信息：<https://keith.github.io/xcode-man-pages/cat.1.html>.

- 将文件内容打印到 `stdout`：

`cat {{path/to/file}}`

- 将多个文件连接成一个输出文件：

`cat {{path/to/file1 path/to/file2 ...}} > {{path/to/output_file}}`

- 将多个文件附加到一个输出文件中：

`cat {{path/to/file1 path/to/file2 ...}} >> {{path/to/output_file}}`

- 无缓冲地将一个文件的内容复制到输出文件：

`cat -u {{/dev/tty12}} > {{/dev/tty13}}`

- 将 `stdin` 写入文件：

`cat - > {{path/to/file}}`

- 为所有输出行编号：

`cat -n {{path/to/file}}`

- 显示不可打印和空白字符（非 ASCII 字符前缀为 `M-`）：

`cat -v -t -e {{path/to/file}}`