# rpcinfo

> 对RPC服务器进行RPC调用并报告其发现的内容。
> 更多信息：<https://manned.org/rpcinfo>。

- 显示在本地主机上注册的所有RPC服务的完整表格：

`rpcinfo`

- 显示在本地主机上注册的所有RPC服务的简明表格：

`rpcinfo -s {{localhost}}`

- 显示本地主机上rpcbind操作的统计信息表：

`rpcinfo -m`

- 显示在远程NFS共享上给定服务名称（mountd）和版本号（2）的条目列表：

`rpcinfo -l {{remote_nfs_server_ip}} {{mountd}} {{2}}`

- 删除所有传输的mountd服务版本1的注册：

`rpcinfo -d {{mountd}} {{1}}`