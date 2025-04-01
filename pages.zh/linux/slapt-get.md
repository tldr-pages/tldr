# slapt-get

> 一个类似于 `apt` 的 Slackware 包管理系统。
> 包源需要在 slapt-getrc 文件中配置。
> 更多信息：<https://software.jaos.org>。

- 更新可用包及其版本列表：

`slapt-get --update`

- 安装一个包，或将其更新到最新可用版本：

`slapt-get --install {{package}}`

- 卸载一个包：

`slapt-get --remove {{package}}`

- 将所有已安装的包更新到最新可用版本：

`slapt-get --upgrade`

- 通过包名、磁盘集或版本查找包：

`slapt-get --search {{query}}`

- 显示关于一个包的信息：

`slapt-get --show {{package}}`
