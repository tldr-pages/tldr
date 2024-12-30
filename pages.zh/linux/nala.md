# nala

> 包管理工具，具有更好的格式化。
> `python-apt` API 的前端。
> 更多信息：<https://gitlab.com/volian/nala>。

- 安装一个软件包，或将其更新到最新可用版本：

`sudo nala install {{package}}`

- 移除一个软件包：

`sudo nala remove {{package}}`

- 移除一个软件包及其配置文件：

`nala purge {{package}}`

- 使用一个词、正则表达式（默认）或通配符搜索软件包名称和描述：

`nala search "{{pattern}}"`

- 更新可用软件包列表并升级系统：

`sudo nala upgrade`

- 从系统中移除所有未使用的软件包和依赖项：

`sudo nala autoremove`

- 获取快速镜像以提高下载速度：

`sudo nala fetch`

- 显示所有事务的历史记录：

`nala history`