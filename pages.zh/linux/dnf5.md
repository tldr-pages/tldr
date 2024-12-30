# dnf5

> 用于 RHEL、Fedora 和 CentOS 的软件包管理工具（它取代了 dnf，而 dnf 又取代了 yum）。
> DNF5 是 DNF 软件包管理器的 C++ 重写版，具有更好的性能和更小的体积。
> 有关其他软件包管理器中等效命令，请参见 <https://wiki.archlinux.org/title/Pacman/Rosetta>。
> 更多信息：<https://dnf5.readthedocs.io>。

- 将已安装的软件包升级到最新可用版本：

`sudo dnf5 upgrade`

- 通过关键字搜索软件包：

`dnf5 search {{keyword1 keyword2 ...}}`

- 显示有关软件包的详细信息：

`dnf5 info {{package}}`

- 安装新软件包（注意：使用 `-y` 自动确认所有提示）：

`sudo dnf5 install {{package1 package2 ...}}`

- 移除软件包：

`sudo dnf5 remove {{package1 package2 ...}}`

- 列出已安装的软件包：

`dnf5 list --installed`

- 查找提供给定命令的软件包：

`dnf5 provides {{command}}`

- 移除或过期缓存数据：

`sudo dnf5 clean all`