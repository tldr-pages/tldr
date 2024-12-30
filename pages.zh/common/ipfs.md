# ipfs

> 行星际文件系统。
> 一种点对点的超媒体协议。旨在使网络更加开放。
> 更多信息：<https://ipfs.io>。

- 从本地添加文件到文件系统，固定并打印相对哈希：

`ipfs add {{path/to/file}}`

- 从本地递归添加目录及其文件到文件系统并打印相对哈希：

`ipfs add -r {{path/to/directory}}`

- 保存远程文件并给它命名，但不固定：

`ipfs get {{hash}} -o {{path/to/file}}`

- 在本地固定远程文件：

`ipfs pin add {{hash}}`

- 显示已固定的文件：

`ipfs pin ls`

- 从本地存储中解除固定文件：

`ipfs pin rm {{hash}}`

- 从本地存储中删除未固定的文件：

`ipfs repo gc`