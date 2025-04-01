# nala

> 包管理工具，格式更好。
> `python-apt` API 的前端工具。
> 更多信息：<https://gitlab.com/volian/nala>。

- 安装一个包，或将其更新到最新版本：

`sudo nala install {{package}}`

- 卸载一个包：

`sudo nala remove {{package}}`

- 卸载一个包及其配置文件：

`nala purge {{package}}`

- 使用单词、正则表达式（默认）或通配符搜索包名和描述：

`nala search "{{pattern}}"`

- 更新可用包列表并升级系统：

`sudo nala upgrade`

- 从系统中移除所有未使用的包和依赖：

`sudo nala autoremove`

- 获取快速镜像以提高下载速度：

`sudo nala fetch`

- 显示所有交易的历史记录：

`nala history`
