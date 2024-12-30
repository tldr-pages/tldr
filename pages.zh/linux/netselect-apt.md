# netselect-apt

> 创建一个用于 Debian 镜像的 `sources.list` 文件，该镜像具有最低延迟。
> 更多信息：<https://manned.org/netselect-apt>。

- 使用最低延迟的服务器创建 `sources.list`：

`sudo netselect-apt`

- 指定 Debian 分支，默认使用稳定版：

`sudo netselect-apt {{testing}}`

- 包含非自由部分：

`sudo netselect-apt --non-free`

- 指定国家以查找镜像列表：

`sudo netselect-apt -c {{India}}`