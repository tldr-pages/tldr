# yum

> RHEL、Fedora 和 CentOS（较旧版本）的包管理工具。
> 其他包管理器的等效命令请参阅：<https://wiki.archlinux.org/title/Pacman/Rosetta>。
> 更多信息：<https://manned.org/yum>。

- 安装新包：

`yum install {{package}}`

- 安装新包并对所有问题自动回答“是”（对更新操作同样有效，适用于自动更新）：

`yum -y install {{package}}`

- 查找提供特定命令的包：

`yum provides {{command}}`

- 移除包：

`yum remove {{package}}`

- 显示已安装包的可用更新：

`yum check-update`

- 将已安装包升级到最新版本：

`yum upgrade`