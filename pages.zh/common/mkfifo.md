# mkfifo

> 创建命名管道，也称为先进先出（FIFO）。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/mkfifo-invocation.html>。

- 在给定路径创建命名管道：

`mkfifo {{路径/到/管道}}`

- 通过命名管道发送数据并将命令发送到后台：

`echo "{{Hello World}}" > {{路径/到/管道}} &`

- 通过命名管道接收数据：

`cat {{路径/到/管道}}`

- 实时共享终端会话：

`mkfifo {{路径/到/管道}}; script {{[-f|--flush]}} {{路径/到/管道}}`
