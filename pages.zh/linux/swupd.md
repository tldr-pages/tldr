# swupd

> Clear Linux 的软件包管理工具。
> 更多信息：<https://www.clearlinux.org/clear-linux-documentation/guides/clear/swupd.html>。

- 更新到最新版本：

`sudo swupd update`

- 显示当前版本，并检查是否有更新版本：

`swupd check-update`

- 列出已安装的捆绑包：

`swupd bundle-list`

- 查找包含所需软件包的捆绑包：

`swupd search -b {{package}}`

- 安装新的捆绑包：

`sudo swupd bundle-add {{bundle}}`

- 移除捆绑包：

`sudo swupd bundle-remove {{bundle}}`

- 修复损坏或丢失的文件：

`sudo swupd verify`