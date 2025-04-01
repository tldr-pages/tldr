# iw dev

> 显示和操作无线设备。
> 有关通道、频率和区域信息的列表： <https://wireless.docs.kernel.org/en/latest/en/developers/documentation/channellist.html>。
> 更多信息： <https://wireless.docs.kernel.org/en/latest/en/users/documentation/iw.html>。

- 设置设备为监控模式（接口必须先关闭。参见 `ip link`）：

`sudo iw dev {{wlp}} set type monitor`

- 设置设备为管理模式（接口必须先关闭）：

`sudo iw dev {{wlp}} set type managed`

- 设置设备的 WiFi 信道（设备必须先设置为监控模式且接口处于打开状态）：

`sudo iw dev {{wlp}} set channel {{channel_number}}`

- 设置设备的 WiFi 频率（MHz）（设备必须先设置为监控模式且接口处于打开状态）：

`sudo iw dev {{wlp}} set freq {{freq_in_mhz}}`

- 显示所有已知的站信息：

`iw dev {{wlp}} station dump`

- 创建具有特定 MAC 地址的虚拟接口，设置为监控模式：

`sudo iw dev {{wlp}} interface add "{{vif_name}}" type monitor addr {{12:34:56:aa:bb:cc}}`

- 删除虚拟接口：

`sudo iw dev "{{vif_name}}" del`