# pacman --sync

> Arch Linux 包管理器工具。
> 另见：`pacman`。
> 更多信息：<https://manned.org/pacman.8>。

- 安装一个新软件包：

`sudo pacman -S {{package}}`

- [S]同步并刷新（[y]）软件包数据库，以及进行系统[u]升级（添加 `--downloadonly` 仅下载软件包而不更新）：

`sudo pacman -Syu`

- 更新并[u]升级所有软件包，并在不提示的情况下安装一个新软件包：

`sudo pacman -Syu --noconfirm {{package}}`

- 在软件包数据库中搜索（[s]）正则表达式或关键词：

`pacman -Ss "{{search_pattern}}"`

- 显示有关软件包的[i]信息：

`pacman -Si {{package}}`

- 在软件包更新期间覆盖冲突文件：

`sudo pacman -Syu --overwrite {{path/to/file}}`

- [S]同步并[u]更新所有软件包，但忽略特定软件包（可以使用多次）：

`sudo pacman -Syu --ignore {{package1 package2 ...}}`

- 从缓存中移除未安装的软件包和未使用的仓库（使用标志 `Sc` 来[c]清理所有软件包）：

`sudo pacman -Sc`