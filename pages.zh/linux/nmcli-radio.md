# nmcli radio

> 显示无线开关的状态或使用 NetworkManager 启用/禁用它们。
> 此子命令也可以使用 `nmcli r` 调用。
> 更多信息：<https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>.

- 显示 Wi-Fi 状态：

`nmcli radio wifi`

- 打开或关闭 Wi-Fi：

`nmcli radio wifi {{on|off}}`

- 显示 WWAN 状态：

`nmcli radio wwan`

- 打开或关闭 WWAN：

`nmcli radio wwan {{on|off}}`

- 显示所有开关的状态：

`nmcli radio all`

- 打开或关闭所有开关：

`nmcli radio all {{on|off}}`