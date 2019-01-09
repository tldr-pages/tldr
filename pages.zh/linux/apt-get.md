# apt-get

> Debian和Ubuntu的软件包管理工具.
> 使用`apt-cache`查找包.

- 更新可用软件包及其版本列表(推荐在其他`apt-get`命令运行之前使用):

`apt-get update`

- 安装一个软件包或更新到最新版本:

`apt-get install {{软件包}}`

- 移除一个软件包:

`apt-get remove {{软件包}}`

- 升级所有已安装软件包到最新版本:

`apt-get upgrade`

- 移除所有不再需要的软件包:

`apt-get autoremove`

- 升级已安装的软件包(类似于`upgrade`), 移除过时的软件包并安装额外的软件包以满足新的依赖:

`apt-get dist-upgrade`
