# dnf5

> 用于 RHEL、Fedora 和 CentOS 的包管理工具（替代了 dnf，而 dnf 本身替代了 yum）。
> DNF5 是 DNF 包管理器的 C++ 重写版本，具有改进的性能和更小的体积。
> 其他包管理器的等效命令，请参见：<https://wiki.archlinux.org/title/Pacman/Rosetta>。
> 更多信息：<https://dnf5.readthedocs.io>。

- 将已安装的包升级到最新版本：

`sudo dnf5 upgrade`

- 通过关键词搜索包：

`dnf5 search {{keyword1 keyword2 ...}}`

- 显示包的详细信息：

`dnf5 info {{package}}`

- 安装新包（注意：使用 `-y` 可自动确认所有提示）：

`sudo dnf5 install {{package1 package2 ...}}`

- 卸载包：

`sudo dnf5 remove {{package1 package2 ...}}`

- 列出已安装的包：

`dnf5 list --installed`

- 查找提供特定命令的包：

`dnf5 provides {{command}}`

- 删除或过期缓存数据：

`sudo dnf5 clean all`