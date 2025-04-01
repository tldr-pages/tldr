# ipfs

> 星际文件系统 (Inter Planetary File System)。
> 一种点对点的超媒体传输协议，旨在使网络更加开放。
> 更多信息：<https://ipfs.io>。

- 从本地添加文件到文件系统，固定它并打印相关哈希值：

`ipfs add {{path/to/file}}`

- 从本地递归添加目录及其文件到文件系统，并打印相关哈希值：

`ipfs add -r {{path/to/directory}}`

- 保存远程文件并指定名称，但不固定：

`ipfs get {{hash}} -o {{path/to/file}}`

- 本地固定远程文件：

`ipfs pin add {{hash}}`

- 显示已固定的文件：

`ipfs pin ls`

- 从本地存储中取消固定文件：

`ipfs pin rm {{hash}}`

- 从本地存储中删除未固定的文件：

`ipfs repo gc`
