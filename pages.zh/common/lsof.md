# lsof

> 列出打开的文件及其对应的进程。
> 注意：需要根权限（或 sudo）才能列出其他用户打开的文件。
> 更多信息：<https://manned.org/lsof>。

- 查找打开特定文件的进程：

`lsof {{path/to/file}}`

- 查找打开本地互联网端口的进程：

`lsof -i :{{port}}`

- 仅输出进程ID（PID）：

`lsof -t {{path/to/file}}`

- 列出指定用户打开的文件：

`lsof -u {{username}}`

- 列出指定命令或进程打开的文件：

`lsof -c {{process_or_command_name}}`

- 列出特定进程打开的文件，给定其 PID：

`lsof -p {{PID}}`

- 列出目录中的打开文件：

`lsof +D {{path/to/directory}}`

- 查找监听本地 IPv6 TCP 端口的进程，并且不转换网络或端口号：

`lsof -i6TCP:{{port}} -sTCP:LISTEN -n -P`