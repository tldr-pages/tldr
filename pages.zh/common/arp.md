# arp

> 显示和操作系统的 ARP 缓存。
> 更多信息：<https://manned.org/arp>。

- 显示当前的 ARP 表：

`arp -a`

- [d] 删除特定条目：

`arp -d {{地址}}`

- [s] 在 ARP 表中设置一个新条目：

`arp -s {{地址}} {{mac_address}}`