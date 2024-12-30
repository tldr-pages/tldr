# 挂载

> 挂载网络文件系统（NFS）网络共享。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/mount>。

- 将共享挂载到 "Z" 驱动器字母：

`mount \\{{computer_name}}\{{share_name}} {{Z:}}`

- 将共享挂载到下一个可用的驱动器字母：

`mount \\{{computer_name}}\{{share_name}} *`

- 以秒为单位挂载共享的读取超时（默认为0.8，可以设置为0.9或1到60）：

`mount -o timeout={{seconds}} \\{{computer_name}}\{{share_name}} {{Z:}}`

- 挂载共享，如果失败则重试最多10次：

`mount -o retry=10 \\{{computer_name}}\{{share_name}} {{Z:}}`

- 强制区分大小写地挂载共享：

`mount -o casesensitive \\{{computer_name}}\{{share_name}} {{Z:}}`

- 作为匿名用户挂载共享：

`mount -o anon \\{{computer_name}}\{{share_name}} {{Z:}}`

- 使用特定挂载类型挂载共享：

`mount -o mtype={{soft|hard}} \\{{computer_name}}\{{share_name}} {{Z:}}`