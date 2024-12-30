# pacman --remove

> Arch Linux 包管理工具。
> 另见: `pacman`。
> 更多信息: <https://manned.org/pacman.8>。

- [R]递归删除一个包及其依赖：

`sudo pacman -Rs {{package}}`

- [R]删除一个包及其依赖。也不保存配置文件的备份：

`sudo pacman -Rsn {{package}}`

- [R]在不提示的情况下删除一个包：

`sudo pacman -R --noconfirm {{package}}`

- [R]删除孤立包（作为[d]ependencies安装但不再被任何包所需）：

`sudo pacman -Rsn $(pacman -Qdtq)`

- [R]删除一个包并[c]ascade到所有依赖于它的包：

`sudo pacman -Rc {{package}}`

- 列出并[p]rint将受到影响的包（不[R]删除任何包）：

`pacman -Rp {{package}}`

- 显示[h]elp：

`pacman -Rh`