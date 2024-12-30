# watch

> 重复执行一个命令，并在全屏模式下监控输出。
> 更多信息：<https://manned.org/watch>。

- 监控当前目录中的文件：

`watch {{ls}}`

- 监控磁盘空间并突出显示变化：

`watch -d {{df}}`

- 监控“node”进程，每 3 秒刷新一次：

`watch -n {{3}} "{{ps aux | grep node}}"`

- 监控磁盘空间，如果有变化则停止监控：

`watch -g {{df}}`