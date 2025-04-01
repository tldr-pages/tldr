# tcpick

> 数据包嗅探和网络流量分析工具。
> 它可以捕获和显示 TCP 连接和数据。它还可以监视接口、主机或端口上的网络流量。
> 更多信息：<https://manned.org/tcpick.8>。

- 在特定接口、端口和主机上捕获流量：

`sudo tcpick {{[-i|--interface]}} {{接口}} {{[-C|--colors]}} -h {{主机}} -p {{端口}}`

- 捕获特定主机上 80 端口（HTTP）的流量：

`sudo tcpick {{[-i|--interface]}} {{eth0}} {{[-C|--colors]}} -h {{192.168.1.100}} -p {{80}}`

- 显示帮助：

`tcpick --help`
