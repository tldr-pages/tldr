# dhcpcd

> DHCP 客户端。
> 更多信息：<https://roy.marples.name/projects/dhcpcd>。

- 释放所有地址租约：

`sudo dhcpcd {{[-k|--release]}}`

- 向 DHCP 服务器请求新的租约：

`sudo dhcpcd {{[-n|--rebind]}}`