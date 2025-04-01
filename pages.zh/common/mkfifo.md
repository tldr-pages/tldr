# mkfifo

> 创建 FIFO（命名管道）。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/mkfifo-invocation.html>.

- 在指定路径创建命名管道：

`mkfifo {{path/to/pipe}}`

- 通过命名管道发送数据，并将命令发送到后台：

`echo "{{Hello World}}" > {{path/to/pipe}} &`

- 通过命名管道接收数据：

`cat {{path/to/pipe}}`

- 实时共享终端会话：

`mkfifo {{path/to/pipe}}; script {{[-f|--flush]}} {{path/to/pipe}}`
