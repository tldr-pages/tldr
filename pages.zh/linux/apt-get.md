# apt-get

> Debian 和 Ubuntu 的软件包管理工具。
> 使用 `apt-cache` 搜索软件包。
> 在 Ubuntu 16.04 及更高版本中，建议在交互式使用时使用 `apt`。
> 更多信息：<https://manned.org/apt-get.8>。

- 更新可用软件包和版本的列表（建议在其他 `apt-get` 命令之前运行此命令）：

`apt-get update`

- 安装一个软件包，或将其更新到最新可用版本：

`apt-get install {{package}}`

- 删除一个软件包：

`apt-get remove {{package}}`

- 删除一个软件包及其配置文件：

`apt-get purge {{package}}`

- 将所有已安装的软件包升级到最新可用版本：

`apt-get upgrade`

- 清理本地存储库 - 删除因下载中断而无法再下载的软件包文件（`.deb`）：

`apt-get autoclean`

- 删除所有不再需要的软件包：

`apt-get autoremove`

- 升级已安装的软件包（类似于 `upgrade`），但删除过时的软件包并安装额外的软件包以满足新的依赖关系：

`apt-get dist-upgrade`