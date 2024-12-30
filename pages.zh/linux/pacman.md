# pacman

> Arch Linux 包管理工具。
> 另见：`pacman-sync`，`pacman-remove`，`pacman-query`，`pacman-upgrade`，`pacman-files`，`pacman-database`，`pacman-deptest`，`pacman-key`，`pacman-mirrors`。
> 有关其他包管理器中的等效命令，请参见 <https://wiki.archlinux.org/title/Pacman/Rosetta>。
> 更多信息：<https://manned.org/pacman.8>。

- [S]ynchronize 和更新所有包：

`sudo pacman -Syu`

- 安装新包：

`sudo pacman -S {{package}}`

- [R]emove 包及其依赖：

`sudo pacman -Rs {{package}}`

- 搜索 ([s]) 包数据库中的正则表达式或关键字：

`pacman -Ss "{{search_pattern}}"`

- 在数据库中搜索包含特定 [F]ile 的包：

`pacman -F "{{file_name}}"`

- 仅列出 [e]xplicitly 安装的包和版本：

`pacman -Qe`

- 列出孤立包（作为 [d]ependencies 安装，但实际上并不被任何包所需）：

`pacman -Qtdq`

- 清空整个 `pacman` 缓存：

`sudo pacman -Scc`