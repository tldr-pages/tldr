# driverquery

> 显示已安装设备驱动程序的信息。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/driverquery>。

- 显示所有已安装设备驱动程序的列表：

`driverquery`

- 以指定格式显示驱动程序列表：

`driverquery /fo {{table|list|csv}}`

- 显示带有列以指示它们是否已签名的驱动程序列表：

`driverquery /si`

- 在输出列表中排除标题：

`driverquery /nh`

- 显示远程计算机的驱动程序列表：

`driverquery /s {{hostname}} /u {{username}} /p {{password}}`

- 显示带有详细信息的驱动程序列表：

`driverquery /v`

- 显示帮助：

`driverquery /?`