# deb-get

> 用于第三方仓库或直接下载发布的 `.deb` 包的 `apt-get` 功能。
> 适用于使用 `apt-get` 的 Linux 发行版。
> 更多信息：<https://github.com/wimpysworld/deb-get>.

- 更新可用软件包及其版本列表：

`deb-get update`

- 搜索指定的软件包：

`deb-get search {{package}}`

- 显示软件包的信息：

`deb-get show {{package}}`

- 安装软件包，或更新至最新可用版本：

`deb-get install {{package}}`

- 移除软件包（使用 `purge` 选项还会移除其配置文件）：

`deb-get remove {{package}}`

- 将所有已安装的软件包升级至最新版本：

`deb-get upgrade`

- 列出所有可用的软件包：

`deb-get list`
