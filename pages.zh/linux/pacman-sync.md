# pacman --sync

> Arch Linux 包管理工具。
> 也请参阅：`pacman`。
> 更多信息：<https://manned.org/pacman.8>。

- 安装新包：

`sudo pacman -S {{package}}`

- 同步并刷新（[y]）包数据库，并进行系统升级（添加 `--downloadonly` 仅下载包而不更新）：

`sudo pacman -Syu`

- 更新并升级所有包并安装新包，不提示确认：

`sudo pacman -Syu --noconfirm {{package}}`

- 在包数据库中搜索正则表达式或关键词：

`pacman -Ss "{{search_pattern}}"`

- 显示关于包的详细信息：

`pacman -Si {{package}}`

- 在包更新时覆盖冲突文件：

`sudo pacman -Syu --overwrite {{path/to/file}}`

- 从缓存中删除未安装的包和未使用的仓库（使用 `Sc` 标志清理所有包）：

`sudo pacman -Sc`

- 指定要安装的包的版本：

`sudo pacman -S {{package}}={{version}}`
