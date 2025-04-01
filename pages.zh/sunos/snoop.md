# snoop

> 网络数据包嗅探器。
> SunOS 版本的 tcpdump。
> 更多信息：<https://www.unix.com/man-page/sunos/1m/snoop>。

- 在特定的网络接口上捕获数据包：

`snoop -d {{e1000g0}}`

- 将捕获的数据包保存到文件中而不是显示在屏幕上：

`snoop -o {{path/to/file}}`

- 从文件中显示数据包的详细协议层摘要：

`snoop -V -i {{path/to/file}}`

- 捕获来自某个主机并前往特定端口的网络数据包：

`snoop to port {{port}} from host {{hostname}}`

- 捕获并显示两个 IP 地址之间交换的网络数据包的十六进制转储：

`snoop -x0 -p4 {{ip1}} {{ip2}}`