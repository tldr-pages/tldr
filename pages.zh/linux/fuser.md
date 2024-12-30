# fuser

> 显示当前使用文件或套接字的进程 ID。
> 更多信息：<https://manned.org/fuser>。

- 查找访问特定文件或目录的进程：

`fuser {{path/to/file_or_directory}}`

- 显示更多字段（`USER`、`PID`、`ACCESS` 和 `COMMAND`）：

`fuser --verbose {{path/to/file_or_directory}}`

- 确定使用 TCP 套接字的进程：

`fuser --namespace tcp {{port}}`

- 杀死所有访问特定文件或目录的进程（发送 `SIGKILL` 信号）：

`fuser --kill {{path/to/file_or_directory}}`

- 查找访问包含特定文件或目录的文件系统的进程：

`fuser --mount {{path/to/file_or_directory}}`

- 杀死所有在特定端口上有 TCP 连接的进程：

`fuser --kill {{port}}/tcp`