# paru

> 一个 AUR 助手和 pacman 包装。
> 更多信息：<https://github.com/Morganamilo/paru>.

- 交互式搜索并安装软件包：

`paru {{包名或关键字}}`

- 同步和更新所有包：

`paru`

- 更新 AUR 包：

`paru -Sua`

- 获取包的信息：

`paru -Si {{包}}`

- 从 AUR 或 ABS 下载 `PKGBUILD` 和其他的包的源文件：

`paru --getpkgbuild {{包}}`

- 显示包的 `PKGBUILD` 文件：

`paru --getpkgbuild --print {{包}}`
