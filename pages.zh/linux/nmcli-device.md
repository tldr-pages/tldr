# nmcli 设备

> 使用 NetworkManager 管理网络接口并建立新的 Wi-Fi 连接。
> 此子命令也可以用 `nmcli d` 调用。
> 更多信息：<https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>。

- 打印所有网络接口的状态：

`nmcli device status`

- 打印可用的 Wi-Fi 接入点：

`nmcli device wifi`

- 连接到指定 SSID 的 Wi-Fi 网络（系统会提示输入密码）：

`nmcli --ask device wifi connect {{ssid}}`

- 打印当前 Wi-Fi 网络的密码和二维码：

`nmcli device wifi show-password`