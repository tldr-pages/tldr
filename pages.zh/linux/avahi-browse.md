# avahi-browse

> 显示通过 mDNS/DNS-SD 在本地网络上暴露的服务和主机。
> Avahi 兼容苹果设备中的 Bonjour (Zeroconf)。
> 更多信息：<https://www.avahi.org/>.

- 列出本地网络上可用的服务及其地址和端口，忽略本地机器上的服务：

`avahi-browse --all --resolve --ignore-local`

- 以 SSV 格式快速列出本地网络中的服务，方便脚本使用：

`avahi-browse --all --terminate --parsable`

- 列出邻域中的域：

`avahi-browse --browse-domains`

- 将搜索限制在特定域内：

`avahi-browse --all --domain={{domain}}`