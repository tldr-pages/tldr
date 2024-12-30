# slapt-get

> 一个类似于 `apt` 的 Slackware 软件包管理系统。
> 软件包源需要在 slapt-getrc 文件中配置。
> 更多信息: <https://software.jaos.org>。

- 更新可用软件包及其版本的列表：

`slapt-get --update`

- 安装一个软件包，或将其更新到最新可用版本：

`slapt-get --install {{package}}`

- 移除一个软件包：

`slapt-get --remove {{package}}`

- 将所有已安装的软件包升级到其最新可用版本：

`slapt-get --upgrade`

- 按软件包名称、磁盘集合或版本查找软件包：

`slapt-get --search {{query}}`

- 显示有关软件包的信息：

`slapt-get --show {{package}}`