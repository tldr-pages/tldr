# opkg

> 一个轻量级的包管理器，用于安装 OpenWrt 包。
> 更多信息：<https://openwrt.org/docs/guide-user/additional-software/opkg>。

- 安装一个包：

`opkg install {{package}}`

- 移除一个包：

`opkg remove {{package}}`

- 更新可用包的列表：

`opkg update`

- 升级一个或多个特定的包：

`opkg upgrade {{package(s)}}`

- 显示特定包的信息：

`opkg info {{package}}`

- 列出所有可用的包：

`opkg list`