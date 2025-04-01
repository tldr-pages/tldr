# showmount

> 显示 Windows Server 上 NFS 文件系统的相关信息。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/showmount>.

- 显示所有导出的文件系统：

`showmount -e`

- 显示所有 NFS 客户端及其挂载的目录：

`showmount -a`

- 显示所有 NFS 挂载的目录：

`showmount -d`

- 显示远程服务器上导出的文件系统：

`showmount -e {{server_address}}`
