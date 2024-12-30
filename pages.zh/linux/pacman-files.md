# pacman --files

> Arch Linux 包管理工具。
> 另见: `pacman`, `pkgfile`。
> 更多信息: <https://manned.org/pacman.8>。

- 更新软件包数据库：

`sudo pacman -Fy`

- 查找拥有特定 [F]ile 的软件包：

`pacman -F {{filename}}`

- 查找拥有特定 [F]ile 的软件包，使用正则表达式 e[x]pression：

`pacman -Fx '{{regular_expression}}'`

- 仅列出软件包名称：

`pacman -Fq {{filename}}`

- [l]列出特定软件包拥有的 [F]iles：

`pacman -Fl {{package}}`

- 显示 [h]elp：

`pacman -Fh`