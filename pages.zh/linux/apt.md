# apt

> 基于Debian的发行版上的软件包管理工具.

- 更新可用软件包及其版本列表(推荐在运行其他apt命令前首先运行该命令):

`sudo apt update`

- 查找指定软件包:

`apt search {{软件包}}`

- 显示关于指定软件包的信息:

`apt show {{软件包}}`

- 安装指定软件包或将指定软件包更新到最新版本:

`sudo apt install {{软件包}}`

- 移除指定软件包(使用`purge`可以同时移除其配置文件):

`sudo apt remove {{软件包}}`

- 将所有已安装软件包更新到最新可用版本:

`sudo apt upgrade`
