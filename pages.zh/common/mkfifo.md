# mkfifo

> 创建 FIFO（命名管道）。
> 更多信息：<https://www.gnu.org/software/coreutils/mkfifo>。

- 在给定路径创建一个命名管道：

`mkfifo {{path/to/pipe}}`

- 通过命名管道发送数据并将命令发送到后台：

`echo "{{Hello World}}" > {{path/to/pipe}} &`

- 通过命名管道接收数据：

`cat {{path/to/pipe}}`

- 实时共享你的终端会话：

`mkfifo {{path/to/pipe}}; script -f {{path/to/pipe}}`