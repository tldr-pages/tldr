# iperf3

> 用于测试网络带宽的流量生成工具。
> 更多信息：<https://iperf.fr>。

- 以服务器模式运行 iperf3：

`iperf3 {{[-s|--server]}}`

- 在指定端口上运行 iperf3 服务器：

`iperf3 {{[-s|--server]}} {{[-p|--port]}} {{port}}`

- 开始带宽测试：

`iperf3 {{[-c|--client]}} {{server}}`

- 以多个并行流运行 iperf3：

`iperf3 {{[-c|--client]}} {{server}} {{[-P|--parallel]}} {{streams}}`

- 反向测试方向，服务器向客户端发送数据：

`iperf3 {{[-c|--client]}} {{server}} {{[-R|--reverse]}}`