# rpcinfo

> 向 RPC 服务器发起 RPC 调用，并报告发现的内容。
> 更多信息：<https://manned.org/rpcinfo>.

- 显示本地主机上注册的所有 RPC 服务的完整表：

`rpcinfo`

- 显示本地主机上注册的所有 RPC 服务的简洁表：

`rpcinfo -s {{localhost}}`

- 显示本地主机上 rpcbind 操作的统计表：

`rpcinfo -m`

- 显示指定服务名称（mountd）和版本号（2）在远程 NFS 服务器上的条目列表：

`rpcinfo -l {{remote_nfs_server_ip}} {{mountd}} {{2}}`

- 删除所有传输中 mountd 服务版本 1 的注册：

`rpcinfo -d {{mountd}} {{1}}`