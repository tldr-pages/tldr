# aptitude

> Debian 和 Ubuntu 上的软件包管理工具.

- 同步可用软件包及其版本列表，在运行后续 aptitude 命令前，应该首先运行该命令:

`aptitude update`

- 安装一个新的软件包及其依赖项:

`aptitude install {{软件包}}`

- 查找软件包:

`aptitude search {{软件包}}`

- 移除一个软件包并移除所有依赖它的软件包:

`aptitude remove {{软件包}}`

- 更新已安装软件包到最新版本:

`aptitude upgrade`

- 更新已安装的软件包（类似于`aptitude upgrade`命令）， 移除过时的软件包并安装额外的软件包以满足新的软件包依赖项:

`aptitude full-upgrade`
