# pacman --files

> Arch Linux 包管理工具。
> 参见：`pacman`，`pkgfile`。
> 更多信息：<https://manned.org/pacman.8>。

- 更新包数据库：

`sudo pacman -Fy`

- 查找拥有特定 [F]ile 的包：

`pacman -F {{filename}}`

- 使用正则表达式查找拥有特定 [F]ile 的包：

`pacman -Fx '{{regular_expression}}'`

- 仅列出包名称：

`pacman -Fq {{filename}}`

- [l]ist the [F]iles owned by a specific package（列出特定包拥有的 [F]iles）：

`pacman -Fl {{package}}`

- 显示 [h]elp（帮助）：

`pacman -Fh`
