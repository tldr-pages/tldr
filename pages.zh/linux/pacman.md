# pacman

> Arch Linux 的软件包管理器工具。
> 另请参阅：`pacman-sync`, `pacman-remove`, `pacman-query`, `pacman-upgrade`, `pacman-files`, `pacman-database`, `pacman-deptest`, `pacman-key`, `pacman-mirrors`。
> 更多信息：<https://manned.org/pacman.8>。

- 同步并更新所有软件包：

`sudo pacman -Syu`

- 安装一个新的软件包：

`sudo pacman -S {{软件包}}`

- 删除一个软件包及其依赖：

`sudo pacman -Rs {{软件包}}`

- 列出已安装的软件包和版本：

`pacman -Q`

- 仅列出明确安装的软件包和版本：

`pacman -Qe`

- 查找哪个包拥有某个文件：

`pacman -Qo {{文件名}}`

- 清空软件包缓存以释放空间：

`sudo pacman -Scc`
