# netselect-apt

> 为延迟最低的 Debian 镜像创建 `sources.list` 文件。
> 更多信息：<https://manned.org/netselect-apt>.

- 使用延迟最低的服务器创建 `sources.list`：

`sudo netselect-apt`

- 指定 Debian 分支，默认使用稳定版：

`sudo netselect-apt {{testing}}`

- 包括非自由软件部分：

`sudo netselect-apt --non-free`

- 指定镜像列表的国家：

`sudo netselect-apt -c {{India}}`
