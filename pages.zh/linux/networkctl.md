# networkctl

> 查询网络链接的状态。
> 使用 `systemd-networkd` 管理网络配置。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/networkctl.html>.

- 列出现有链接及其状态：

`networkctl list`

- 显示网络总体状态：

`networkctl status`

- 启用网络设备：

`networkctl up {{interface1 interface2 ...}}`

- 禁用网络设备：

`networkctl down {{interface1 interface2 ...}}`

- 刷新动态配置（例如从 DHCP 服务器接收的 IP 地址）：

`networkctl renew {{interface1 interface2 ...}}`

- 重新加载配置文件（.netdev 和 .network）：

`networkctl reload`

- 重新配置网络接口（如果编辑了配置文件，需要先调用 `networkctl reload`）：

`networkctl reconfigure {{interface1 interface2 ...}}`