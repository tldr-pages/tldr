# netperf

> `netperf` 客户端命令，用于测量网络吞吐量的基准测试应用。类似于 `iperf`。
> 参见：`netserver`，服务器端命令。
> 更多信息：<https://hewlettpackard.github.io/netperf/doc/netperf.html#Global-Command_002dline-Options>.

- 通过默认端口（12865）连接到指定 IP 地址的服务器：

`netperf {{address}}`

- 指定 [p]ort（端口）：

`netperf {{address}} -p {{port}}`

- 指定采样 [l]ength（持续时间，以秒为单位，默认为 10 秒）：

`netperf {{address}} -l {{seconds}}`

- 强制使用 IPv[4] 或 IPv[6]：

`netperf {{address}} -{{4|6}}`
