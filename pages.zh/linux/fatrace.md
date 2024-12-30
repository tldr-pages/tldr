# fatrace

> 报告文件访问事件。
> 更多信息：<https://manned.org/fatrace>。

- 将所有已挂载文件系统的文件访问事件打印到 `stdout`：

`sudo fatrace`

- 将当前目录挂载上的文件访问事件（带时间戳）打印到 `stdout`：

`sudo fatrace {{-c|--current-mount}} {{-t|--timestamp}}`