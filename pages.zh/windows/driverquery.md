# driverquery

> 显示已安装设备驱动程序的信息。
> 更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/driverquery>.

- 显示所有已安装设备驱动程序的列表：

`driverquery`

- 以指定格式显示驱动程序的列表：

`driverquery /fo {{table|list|csv}}`

- 显示带有列的驱动程序列表，以表明它们是否已签名：

`driverquery /si`

- 排除输出列表中的标题：

`driverquery /nh`

- 显示远程计算机的驱动程序列表：

`driverquery /s {{主机名}} /u {{用户名}} /p {{密码}}`

- 显示详细信息的驱动程序列表：

`driverquery /v`

- 显示详细的使用信息：

`driverquery /?`
