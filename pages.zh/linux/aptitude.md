# aptitude

> Debian 和 Ubuntu 的软件包管理工具。
> 更多信息：<https://manned.org/aptitude.8>。

- 同步可用的软件包和版本列表。应首先运行此命令，然后再运行后续的 `aptitude` 命令：

`aptitude update`

- 安装一个新软件包及其依赖项：

`aptitude install {{package}}`

- 搜索一个软件包：

`aptitude search {{package}}`

- 搜索已安装的软件包（`?installed` 是一个 `aptitude` 搜索术语）：

`aptitude search '?installed({{package}})'`

- 删除一个软件包及其所有依赖于它的软件包：

`aptitude remove {{package}}`

- 将已安装的软件包升级到最新可用版本：

`aptitude upgrade`

- 升级已安装的软件包（类似于 `aptitude upgrade`），包括删除过时的软件包和安装额外的软件包以满足新的软件包依赖关系：

`aptitude full-upgrade`

- 将已安装的软件包置为保留状态，以防止其被自动升级：

`aptitude hold '?installed({{package}})'`