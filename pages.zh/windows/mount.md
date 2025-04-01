# mount

> 挂载网络文件系统（NFS）网络共享。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/mount>.

- 将共享挂载到“Z”驱动器：

`mount \\{{computer_name}}\{{share_name}} {{Z:}}`

- 将共享挂载到下一个可用的驱动器：

`mount \\{{computer_name}}\{{share_name}} *`

- 使用读取超时时间（默认为0.8秒，可以设置为0.9或1到60秒）挂载共享：

`mount -o timeout={{seconds}} \\{{computer_name}}\{{share_name}} {{Z:}}`

- 如果挂载失败，重试10次：

`mount -o retry=10 \\{{computer_name}}\{{share_name}} {{Z:}}`

- 强制区分大小写挂载共享：

`mount -o casesensitive \\{{computer_name}}\{{share_name}} {{Z:}}`

- 以匿名用户身份挂载共享：

`mount -o anon \\{{computer_name}}\{{share_name}} {{Z:}}`

- 使用特定挂载类型挂载共享：

`mount -o mtype={{soft|hard}} \\{{computer_name}}\{{share_name}} {{Z:}}`
