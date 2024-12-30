# deb-get

> `apt-get` 功能用于在第三方仓库或通过直接下载发布的 `.deb` 包。
> 适用于使用 `apt-get` 的 Linux 发行版。
> 更多信息：<https://github.com/wimpysworld/deb-get>。

- 更新可用包和版本的列表：

`deb-get update`

- 搜索给定的包：

`deb-get search {{package}}`

- 显示有关包的信息：

`deb-get show {{package}}`

- 安装一个包，或将其更新到最新可用版本：

`deb-get install {{package}}`

- 移除一个包（使用 `purge` 还会移除其配置文件）：

`deb-get remove {{package}}`

- 将所有已安装的包升级到最新可用版本：

`deb-get upgrade`

- 列出所有可用的包：

`deb-get list`