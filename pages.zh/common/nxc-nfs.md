# nxc nfs

> 渗透测试和利用 NFS 服务器。目前仅支持匿名模式。
> 更多信息：<https://www.netexec.wiki/nfs-protocol>.

- 检测远程 NFS 服务器的版本：

`nxc nfs {{192.168.178.0/24}}`

- 列出可用的 NFS 共享：

`nxc nfs {{192.168.178.2}} --shares`

- 递归枚举指定深度的共享目录：

`nxc nfs {{192.168.178.2}} --enum-shares {{5}}`

- 下载指定的远程文件：

`nxc nfs {{192.168.178.2}} --get-file {{path/to/remote_file}} {{path/to/local_file}}`

- 将指定的本地文件上传到远程共享：

`nxc nfs {{192.168.178.2}} --put-file {{path/to/local_file}} {{path/to/remote_file}}`