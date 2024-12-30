# paru

> 一个 AUR 助手和 pacman 封装器。
> 更多信息：<https://github.com/Morganamilo/paru>。

- 交互式搜索并安装一个软件包：

`paru {{package_name_or_search_term}}`

- 同步并更新所有软件包：

`paru`

- 升级 AUR 软件包：

`paru -Sua`

- 获取有关软件包的信息：

`paru -Si {{package}}`

- 从 AUR 或 ABS 下载 `PKGBUILD` 和其他软件包源文件：

`paru --getpkgbuild {{package}}`

- 显示一个软件包的 `PKGBUILD` 文件：

`paru --getpkgbuild --print {{package}}`