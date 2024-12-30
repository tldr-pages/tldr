# yum

> RHEL、Fedora 和 CentOS（旧版本）的包管理工具。
> 有关其他包管理器中等效命令，请参见 <https://wiki.archlinux.org/title/Pacman/Rosetta>。
> 更多信息请访问：<https://manned.org/yum>。

- 安装新包：

`yum install {{package}}`

- 安装新包并对所有问题假设为“是”（也适用于更新，非常适合自动更新）：

`yum -y install {{package}}`

- 查找提供特定命令的包：

`yum provides {{command}}`

- 移除包：

`yum remove {{package}}`

- 显示已安装包的可用更新：

`yum check-update`

- 将已安装的包升级到最新可用版本：

`yum upgrade`