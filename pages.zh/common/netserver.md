# netserver

> `netperf` 的服务器端命令，`netperf` 是一个用于测量网络吞吐量的基准测试应用程序。
> 参见：`netperf`，用于客户端命令。
> 更多信息：<https://manned.org/netserver.1>.

- 在默认端口（12865）上启动服务器并分叉到后台：

`netserver`

- 在前台启动服务器，不进行分叉：

`netserver -D`

- 指定 [p]ort（端口）：

`netserver -p {{port}}`

- 强制使用 IPv[4] 或 IPv[6]：

`netserver -{{4|6}}`