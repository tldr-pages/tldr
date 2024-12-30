# iperf3

> 用于测试网络带宽的流量生成器。
> 更多信息：<https://iperf.fr>。

- 作为服务器运行 iperf3：

`iperf3 -s`

- 在特定端口上运行 iperf3 服务器：

`iperf3 -s -p {{port}}`

- 开始带宽测试：

`iperf3 -c {{server}}`

- 在多个并行流中运行 iperf3：

`iperf3 -c {{server}} -P {{streams}}`

- 反向测试方向。服务器向客户端发送数据：

`iperf3 -c {{server}} -R`