# aptitude

> Debian 和 Ubuntu 上的软件包管理工具。
> 更多信息：<https://manned.org/aptitude>。

- 同步可用软件包及其版本列表，在运行后续 aptitude 命令前，应该首先运行该命令：

`sudo aptitude update`

- 安装一个新的软件包及其依赖：

`sudo aptitude install {{软件包}}`

- 查找一个软件包：

`aptitude search {{软件包}}`

- 查找一个已安装的软件包（`?installed` 是一个 aptitude 搜索项）：

`aptitude search '?installed({{软件包}})'`

- 移除一个软件包并移除所有依赖它的软件包：

`sudo aptitude remove {{软件包}}`

- 更新已安装软件包到最新版本：

`sudo aptitude upgrade`

- 更新已安装的软件包（类似于 `aptitude upgrade` 命令），移除过时的软件包并安装额外的软件包以满足新的软件包依赖项：

`sudo aptitude full-upgrade`

- 锁定一个已安装的软件包以便阻止它自动升级：

`sudo aptitude hold '?installed({{软件包}})'`
