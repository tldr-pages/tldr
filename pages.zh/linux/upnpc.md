# upnpc

> 通过UPnP协议配置路由器上的端口转发规则。
> 更多信息：<https://manned.org/upnpc>。

- 将外部TCP端口80转发到本地机器的8080端口：

`upnpc -a {{192.168.0.1}} 8080 80 tcp`

- 删除外部TCP端口80的任何端口重定向：

`upnpc -d 80 tcp`

- 获取网络上UPnP设备的信息：

`upnpc -s`

- 列出现有的重定向：

`upnpc -l`