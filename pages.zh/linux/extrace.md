# extrace

> 跟踪 exec() 调用。
> 更多信息：<https://github.com/chneukirchen/extrace>。

- 跟踪系统上发生的所有程序执行：

`sudo extrace`

- 运行一个命令并仅跟踪该命令的子进程：

`sudo extrace {{command}}`

- 打印每个进程的当前工作目录：

`sudo extrace -d`

- 解析每个可执行文件的完整路径：

`sudo extrace -l`

- 显示运行每个进程的用户：

`sudo extrace -u`