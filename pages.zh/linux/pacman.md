# pacman

> Arch Linux 的软件包管理器工具。

- 同步并更新所有软件包：

`pacman -Syu`

- 安装一个新的软件包：

`pacman -S {{package_name}}`

- 删除一个软件包及其依赖：

`pacman -Rs {{package_name}}`

- 在软件包数据库中搜索正则表达式或关键字：

`pacman -Ss "{{search_pattern}}"`

- 列出已安装的软件包和版本：

`pacman -Q`

- 仅列出明确安装的软件包和版本：

`pacman -Qe`

- 查找哪个包拥有某个文件：

`pacman -Qo {{filename}}`

- 清空软件包缓存以释放空间：

`pacman -Scc`
