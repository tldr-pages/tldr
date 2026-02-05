# zerotier-cli

> 控制本地的 ZeroTier 虚拟网络服务。
> 另请参阅：`zerotier-idtool`, `zerotier-one`。
> 更多信息：<https://github.com/zerotier/ZeroTierOne/blob/main/doc/zerotier-cli.1.md>。

- 加入一个网络：

`sudo zerotier-cli join {{网络 ID}}`

- 列出网络：

`sudo zerotier-cli listnetworks`

- 以可读格式列出对等节点：

`sudo zerotier-cli peers`

- 离开一个网络：

`sudo zerotier-cli leave {{网络 ID}}`

- 显示 ZeroTier One 的状态：

`sudo zerotier-cli {{[info|status]}}`
