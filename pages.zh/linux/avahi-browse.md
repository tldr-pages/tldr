# avahi-browse

> 显示通过 mDNS/DNS-SD 暴露在本地网络的服务和主机。
> Avahi 与苹果设备的 Bonjour（Zeroconf）兼容。
> 更多信息：<https://www.avahi.org/>.

- 列出本地网络中的所有服务和他们的地址与端口，忽略他们本地的地址和端口：

`avahi-browse --all --resolve --ignore-local`

- 列出所有的域名：

`avahi-browse --browse-domains`

- 只搜索一个特定的域名：

`avahi-browse --all --domain={{domain}}`
