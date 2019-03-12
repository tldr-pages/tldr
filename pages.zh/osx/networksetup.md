# networksetup

> 网络系统首选项配置工具.

- 列出可用的网络服务源（以太网、Wi-Fi、蓝牙等）:

`networksetup -listallnetworkservices`

- 显示特定网络设备的配置信息:

`networksetup -getinfo {{"Wi-Fi"}}`

- 获取当前连接的Wi-Fi网络名称（Wi-Fi设备通常为en0或en1）:

`networksetup -getairportnetwork {{en0}}`

- 连接到给定的Wi-Fi网络Connect to a particular Wi-Fi network:

`networksetup -setairportnetwork {{en0}} {{"无线网SSID"}} {{密码}}`
