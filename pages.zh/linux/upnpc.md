# upnpc

> 通过 UPnP 协议在路由器上配置端口转发规则。
> 更多信息：<https://manned.org/upnpc>.

- 将外部 TCP 端口 80 转发到本地机器的 8080 端口：

`upnpc -a {{192.168.0.1}} 8080 80 tcp`

- 删除外部 TCP 端口 80 的任何端口重定向：

`upnpc -d 80 tcp`

- 获取网络上 UPnP 设备的信息：

`upnpc -s`

- 列出现有的端口重定向：

`upnpc -l`
