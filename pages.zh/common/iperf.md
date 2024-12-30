# iperf

> 测量计算机之间的网络带宽。
> 更多信息: <https://iperf.fr>。

- 在服务器上运行：

`iperf -s`

- 在服务器上以UDP模式运行并将服务器端口设置为监听5001：

`iperf -u -s -p {{5001}}`

- 在客户端运行：

`iperf -c {{server_address}}`

- 每2秒在客户端运行：

`iperf -c {{server_address}} -i {{2}}`

- 在客户端以5个并行线程运行：

`iperf -c {{server_address}} -P {{5}}`

- 在客户端使用UDP模式运行：

`iperf -u -c {{server_address}} -p {{5001}}`