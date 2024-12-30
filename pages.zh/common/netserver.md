# netserver

> `netperf` 的服务器端命令，该基准测试应用程序用于测量网络吞吐量。
> 另见：`netperf`，用于客户端的命令。
> 更多信息：<https://manned.org/netserver.1>。

- 在默认端口（12865）上启动服务器并在后台运行：

`netserver`

- 在前台启动服务器并不进行分叉：

`netserver -D`

- 指定 [p]ort：

`netserver -p {{port}}`

- 强制使用 IPv[4] 或 IPv[6]：

`netserver -{{4|6}}`