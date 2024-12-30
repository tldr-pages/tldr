# wajig

> 针对基于Debian系统的简化一体化系统支持工具。
> 更多信息：<https://wajig.togaware.com>。

- 更新可用软件包和版本的列表：

`wajig update`

- 安装一个软件包，或将其更新到最新可用版本：

`wajig install {{package}}`

- 移除一个软件包及其配置文件：

`wajig purge {{package}}`

- 执行更新，然后进行发行版升级：

`wajig daily-upgrade`

- 显示已安装软件包的大小：

`wajig sizes`

- 列出所有已安装软件包的版本和发行版：

`wajig versions`

- 列出可升级软件包的版本：

`wajig toupgrade`

- 显示与给定软件包有某种依赖关系的软件包：

`wajig dependents {{package}}`