# zypper

> SUSE 和 openSUSE 的软件包管理工具。
> 有关其他软件包管理器中等效命令的信息，请参见 <https://wiki.archlinux.org/title/Pacman/Rosetta>。
> 更多信息：<https://en.opensuse.org/SDB:Zypper_manual>。

- 同步可用软件包和版本的列表：

`zypper refresh`

- 安装新软件包：

`zypper install {{package}}`

- 移除软件包：

`zypper remove {{package}}`

- 升级已安装的软件包到最新可用版本：

`zypper update`

- 通过关键字搜索软件包：

`zypper search {{keyword}}`

- 显示与配置的仓库相关的信息：

`zypper repos --sort-by-priority`