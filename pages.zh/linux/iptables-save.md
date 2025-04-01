# iptables-save

> 保存 `iptables` 的 IPv4 配置。
> 使用 `ip6tables-save` 来保存 IPv6 的配置。
> 更多信息：<https://manned.org/iptables-save>.

- 打印 `iptables` 配置：

`sudo iptables-save`

- 打印特定表的 `iptables` 配置：

`sudo iptables-save {{[-t|--table]}} {{table}}`

- 将 `iptables` 配置保存到文件：

`sudo iptables-save {{[-f|--file]}} {{path/to/file}}`