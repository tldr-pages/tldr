# pivpn

> 简易的安全增强版 OpenVPN 设置和管理工具。
> 最初为 Raspberry Pi 设计，但也可以在其他 Linux 设备上使用。
> 更多信息请访问: <https://www.pivpn.io/>。

- 添加一个新客户端设备：

`sudo pivpn add`

- 列出所有客户端设备：

`sudo pivpn list`

- 列出当前连接的设备及其统计信息：

`sudo pivpn clients`

- 撤销先前认证的设备：

`sudo pivpn revoke`

- 卸载 PiVPN：

`sudo pivpn uninstall`