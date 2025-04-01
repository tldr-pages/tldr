# resolvectl

> 解析域名、IPv4 和 IPv6 地址、DNS 资源记录和服务。
> 检查和重新配置 DNS 解析器。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/resolvectl.html>。

- 显示 DNS 设置：

`resolvectl status`

- 解析一个或多个域名的 IPv4 和 IPv6 地址：

`resolvectl query {{domain1 domain2 ...}}`

- 获取指定 IP 地址的域名：

`resolvectl query {{ip_address}}`

- 清除所有本地 DNS 缓存：

`resolvectl flush-caches`

- 显示 DNS 统计信息（事务、缓存和 DNSSEC 判决）：

`resolvectl statistics`

- 获取域名的 MX 记录：

`resolvectl --legend={{no}} --type={{MX}} query {{domain}}`

- 解析 SRV 记录，例如 _xmpp-server._tcp gmail.com：

`resolvectl service _{{service}}._{{protocol}} {{name}}`

- 获取 TLS 密钥：

`resolvectl tlsa tcp {{domain}}:443`
