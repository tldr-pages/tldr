# dnf

> RHEL、Fedora 和 CentOS 的包管理工具（替代 yum）。
> 一些子命令如 `group` 和 `config-manager` 有自己的使用文档。
> 有关其他包管理器中等效命令的信息，请参阅 <https://wiki.archlinux.org/title/Pacman/Rosetta>。
> 更多信息：<https://dnf.readthedocs.io>。

- 将已安装的软件包升级到最新可用版本：

`sudo dnf upgrade`

- 通过关键字搜索软件包：

`dnf search {{keyword1 keyword2 ...}}`

- 显示有关软件包的详细信息：

`dnf info {{package}}`

- 安装新软件包（使用 `-y` 自动确认所有提示）：

`sudo dnf install {{package1 package2 ...}}`

- 移除软件包：

`sudo dnf remove {{package1 package2 ...}}`

- 列出已安装的软件包：

`dnf list --installed`

- 查找提供给定命令的软件包：

`dnf provides {{command}}`

- 查看所有过去的操作：

`dnf history`