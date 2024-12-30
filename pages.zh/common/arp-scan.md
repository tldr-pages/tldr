# arp-scan

> 发送 ARP 数据包到主机（指定为 IP 地址或主机名）以扫描本地网络。
> 更多信息：<https://github.com/royhills/arp-scan>。

- 扫描当前本地网络：

`arp-scan --localnet`

- 使用自定义位掩码扫描 IP 网络：

`arp-scan {{192.168.1.1}}/{{24}}`

- 在自定义范围内扫描 IP 网络：

`arp-scan {{127.0.0.0}}-{{127.0.0.31}}`

- 使用自定义子网掩码扫描 IP 网络：

`arp-scan {{10.0.0.0}}:{{255.255.255.0}}`