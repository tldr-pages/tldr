# iperf

> 测量计算机之间的网络带宽。
> 更多信息：<https://iperf.fr>。

- 在服务器上运行：

`iperf {{[-s|--server]}}`

- 在服务器上使用 UDP 模式并设置监听端口为 5001：

`iperf {{[-u|--udp]}} {{[-s|--server]}} {{[-p|--port]}} {{5001}}`

- 在客户端上运行：

`iperf {{[-c|--client]}} {{server_address}}`

- 每 2 秒在客户端上运行一次：

`iperf {{[-c|--client]}} {{server_address}} {{[-i|--interval]}} {{2}}`

- 在客户端上使用 5 个并行线程运行：

`iperf {{[-c|--client]}} {{server_address}} {{[-P|--parallel]}} {{5}}`

- 在客户端上使用 UDP 模式运行：

`iperf {{[-u|--udp]}} {{[-c|--client]}} {{server_address}} {{[-p|--port]}} {{5001}}`
