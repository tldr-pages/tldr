# iw dev

> 显示和操作无线设备。
> 有关频道、频率和注册信息的列表：<https://wireless.docs.kernel.org/en/latest/en/developers/documentation/channellist.html>。
> 更多信息：<https://wireless.docs.kernel.org/en/latest/en/users/documentation/iw.html>。

- 将设备设置为监控模式（接口必须先关闭。另请参见 `ip link`）：

`sudo iw dev {{wlp}} set type monitor`

- 将设备设置为管理模式（接口必须先关闭）：

`sudo iw dev {{wlp}} set type managed`

- 设置设备的WiFi频道（设备必须首先处于监控模式且接口已开启）：

`sudo iw dev {{wlp}} set channel {{channel_number}}`

- 设置设备的WiFi频率（单位为MHz，设备必须首先处于监控模式且接口已开启）：

`sudo iw dev {{wlp}} set freq {{freq_in_mhz}}`

- 显示所有已知的站点信息：

`iw dev {{wlp}} station dump`

- 以特定MAC地址创建一个监控模式的虚拟接口：

`sudo iw dev {{wlp}} interface add "{{vif_name}}" type monitor addr {{12:34:56:aa:bb:cc}}`

- 删除虚拟接口：

`sudo iw dev "{{vif_name}}" del`