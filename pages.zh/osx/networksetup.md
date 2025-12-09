# networksetup

> 网络系统首选项配置工具。
> 更多信息：<https://support.apple.com/guide/remote-desktop/about-networksetup-apdd0c5a2d5/mac>.

- 列出可用的网络服务源（以太网、Wi-Fi、蓝牙等）：

`networksetup -listallnetworkservices`

- 显示特定网络设备的配置信息：

`networksetup -getinfo "{{Wi-Fi}}"`

- 获取当前连接的 Wi-Fi 网络名称（Wi-Fi 设备通常为 en0 或 en1）：

`networksetup -getairportnetwork {{en0}}`

- 连接到给定的 Wi-Fi 网络 Connect to a particular Wi-Fi network：

`networksetup -setairportnetwork {{en0}} {{无线网 SSID}} {{密码}}`
