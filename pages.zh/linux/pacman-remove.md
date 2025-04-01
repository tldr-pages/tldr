# pacman --remove

> Arch Linux 软件包管理工具。
> 参见: `pacman`。
> 更多信息: <https://manned.org/pacman.8>。

- [R]移除一个软件包及其所有依赖项并递归地移除它们：

`sudo pacman -Rs {{package}}`

- [R]移除一个软件包及其所有依赖项，同时不保留配置文件的备份：

`sudo pacman -Rsn {{package}}`

- [R]移除一个软件包而不提示确认：

`sudo pacman -R --noconfirm {{package}}`

- [R]移除孤儿包（作为依赖项安装但没有任何软件包需要的包）：

`sudo pacman -Rsn $(pacman -Qdtq)`

- [R]移除一个软件包，并级联移除依赖于它的所有软件包：

`sudo pacman -Rc {{package}}`

- 列出并[p]打印将被影响的软件包（不会[R]移除任何软件包）：

`pacman -Rp {{package}}`

- 显示[h]帮助：

`pacman -Rh`