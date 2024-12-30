# nmcli 无线电

> 显示无线开关的状态或使用 NetworkManager 启用/禁用它们。
> 此子命令也可以通过 `nmcli r` 调用。
> 更多信息：<https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>。

- 显示 Wi-Fi 状态：

`nmcli radio wifi`

- 开启或关闭 Wi-Fi：

`nmcli radio wifi {{on|off}}`

- 显示 WWAN 状态：

`nmcli radio wwan`

- 开启或关闭 WWAN：

`nmcli radio wwan {{on|off}}`

- 显示两个开关的状态：

`nmcli radio all`

- 开启或关闭两个开关：

`nmcli radio all {{on|off}}`