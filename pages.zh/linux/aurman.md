# aurman

> 一个用于从 Arch 用户库构建和安装软件包的 Arch Linux 工具。
> 另见 `pacman`。
> 更多信息：<https://github.com/polygamma/aurman>。

- 同步并更新所有软件包：

`aurman --sync --refresh --sysupgrade`

- 同步并更新所有软件包，不显示 `PKGBUILD` 文件的更改：

`aurman --sync --refresh --sysupgrade --noedit`

- 安装一个新软件包：

`aurman --sync {{package}}`

- 安装一个新软件包，不显示 `PKGBUILD` 文件的更改：

`aurman --sync --noedit {{package}}`

- 安装一个新软件包时不提示：

`aurman --sync --noedit --noconfirm {{package}}`

- 在官方库和 AUR 中搜索软件包数据库中的关键词：

`aurman --sync --search {{keyword}}`

- 移除一个软件包及其依赖项：

`aurman --remove --recursive --nosave {{package}}`

- 清除软件包缓存（使用两个 `--clean` 标志以清除所有软件包）：

`aurman --sync --clean`