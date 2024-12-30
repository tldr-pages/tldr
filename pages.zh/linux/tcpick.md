# tcpick

> 数据包嗅探和网络流量分析工具。
> 它可以捕获并显示TCP连接和数据。它还可以监控特定接口、主机或端口上的网络流量。
> 更多信息：<https://manned.org/tcpick.8>。

- 在特定的[i]nterface、端口和主机上捕获流量：

`sudo tcpick -i {{interface}} -C -h {{host}} -p {{port}}`

- 在特定主机的80端口（HTTP）上捕获流量：

`sudo tcpick -i {{eth0}} -C -h {{192.168.1.100}} -p {{80}}`

- 显示帮助信息：

`tcpick --help`