# arp

> 显示和操作系统的ARP缓存.

- 显示当前的ARP表:

`arp -a`

- 清除整个缓存:

`sudo arp -a -d`

- 删除特定条目:

`arp -d {{address}}`

- 创建指定条目:

`arp -s {{address}} {{mac_address}}`
