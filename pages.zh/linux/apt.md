# apt

> 针对基于Debian的发行版的包管理工具。
> 在Ubuntu 16.04及更高版本中，推荐在交互式使用时替代`apt-get`。
> 有关其他包管理器中等效命令的信息，请参见<https://wiki.archlinux.org/title/Pacman/Rosetta>。
> 更多信息：<https://manned.org/apt.8>。

- 更新可用包和版本的列表（建议在其他`apt`命令之前运行此命令）：

`sudo apt update`

- 搜索给定的包：

`apt search {{package}}`

- 显示包的信息：

`apt show {{package}}`

- 安装一个包，或将其更新到最新可用版本：

`sudo apt install {{package}}`

- 移除一个包（使用`purge`则同时移除其配置文件）：

`sudo apt remove {{package}}`

- 将所有已安装的包升级到最新可用版本：

`sudo apt upgrade`

- 列出所有包：

`apt list`

- 列出已安装的包：

`apt list --installed`