# auracle

> 用于与 Arch Linux 的用户仓库（通常称为 AUR）交互的命令行工具。
> 更多信息请访问：<https://github.com/falconindy/auracle>。

- 显示匹配正则表达式的 AUR 包：

`auracle search '{{正则表达式}}'`

- 显示一个或多个 AUR 包的信息：

`auracle info {{包名1 包名2 ...}}`

- 显示一个或多个 AUR 包的 `PKGBUILD` 文件（构建信息）：

`auracle show {{包名1 包名2 ...}}`

- 显示已安装 AUR 包的更新：

`auracle outdated`