# netperf

> `netperf` 的客户端命令，基准测试应用程序，用于测量网络吞吐量。类似于 `iperf`。
> 另请参见：`netserver`，用于服务器端命令。
> 更多信息：<https://hewlettpackard.github.io/netperf/doc/netperf.html#Global-Command_002dline-Options>。

- 通过默认端口（12865）连接到特定 IP 地址的服务器：

`netperf {{address}}`

- 指定 [p]ort：

`netperf {{address}} -p {{port}}`

- 指定采样 [l]ength（以秒为单位，默认值为 10）：

`netperf {{address}} -l {{seconds}}`

- 强制使用 IPv[4] 或 IPv[6]：

`netperf {{address}} -{{4|6}}`