# iwlist

> 从无线接口获取详细信息。
> 更多信息：<https://manned.org/iwlist.8>。

- 显示范围内的接入点和临时网络单元列表：

`iwlist {{wireless_interface}} scan`

- 显示设备中可用的频率：

`iwlist {{wireless_interface}} frequency`

- 列出设备支持的比特率：

`iwlist {{wireless_interface}} rate`

- 列出当前设置的WPA认证参数：

`iwlist {{wireless_interface}} auth`

- 列出设备中设置的所有WPA加密密钥：

`iwlist {{wireless_interface}} wpakeys`

- 列出支持的加密密钥大小，并列出设备中设置的所有加密密钥：

`iwlist {{wireless_interface}} keys`

- 列出设备的各种电源管理属性和模式：

`iwlist {{wireless_interface}} power`

- 列出设备中设置的通用信息元素（用于WPA支持）：

`iwlist {{wireless_interface}} genie`