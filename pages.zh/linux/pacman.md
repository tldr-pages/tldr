# pacman

> Arch Linux 的软件包管理器工具。
> 更多信息：<https://man.archlinux.org/man/pacman.8>.

- 同步并更新所有软件包：

`sudo pacman --sync --refresh --sysupgrade`

- 安装一个新的软件包：

`sudo pacman --sync {{软件包}}`

- 删除一个软件包及其依赖：

`sudo pacman --remove --recursive {{软件包}}`

- 在软件包数据库中搜索正则表达式或关键字：

`pacman --sync --search "{{软件包}}"`

- 列出已安装的软件包和版本：

`pacman --query`

- 仅列出明确安装的软件包和版本：

`pacman --query --explicit`

- 查找哪个包拥有某个文件：

`pacman --query --owns {{文件名}}`

- 清空软件包缓存以释放空间：

`sudo pacman --sync --clean --clean`
