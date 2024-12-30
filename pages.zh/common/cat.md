# cat

> 打印和连接文件。
> 更多信息：<https://manned.org/cat.1posix>。

- 将文件的内容打印到 `stdout`：

`cat {{path/to/file}}`

- 将多个文件连接成一个输出文件：

`cat {{path/to/file1 path/to/file2 ...}} > {{path/to/output_file}}`

- 将多个文件附加到输出文件：

`cat {{path/to/file1 path/to/file2 ...}} >> {{path/to/output_file}}`

- 将文件的内容复制到输出文件而不进行缓冲：

`cat -u {{/dev/tty12}} > {{/dev/tty13}}`

- 将 `stdin` 写入文件：

`cat - > {{path/to/file}}`