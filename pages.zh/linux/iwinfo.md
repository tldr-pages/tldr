# iwinfo

> 获取 OpenWrt 上无线接口的信息。
> 更多信息：<https://openwrt.org/docs/guide-developer/ubus/iwinfo>。

- 列出所有可用的无线接口：

`iwinfo`

- 显示特定无线接口的详细信息：

`iwinfo {{interface}} info`

- 扫描接口能看到的附近无线网络：

`iwinfo {{interface}} scan`

- 列出已连接的设备：

`iwinfo {{interface}} assoclist`

- 列出接口支持的信道：

`iwinfo {{interface}} freqlist`

- 列出接口可用的发射功率等级：

`iwinfo {{interface}} txpowerlist`

- 显示帮助：

`iwinfo h`
