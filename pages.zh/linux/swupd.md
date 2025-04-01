# swupd

> Clear Linux 的软件包管理工具。
> 更多信息：<https://www.clearlinux.org/clear-linux-documentation/guides/clear/swupd.html>。

- 更新到最新版本：

`sudo swupd update`

- 显示当前版本，并检查是否有更新版本：

`swupd check-update`

- 列出已安装的软件包集：

`swupd bundle-list`

- 查找特定软件包所在的软件包集：

`swupd search -b {{package}}`

- 安装新的软件包集：

`sudo swupd bundle-add {{bundle}}`

- 移除软件包集：

`sudo swupd bundle-remove {{bundle}}`

- 修复损坏或缺失的文件：

`sudo swupd verify`