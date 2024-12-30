# slapt-src

> 一个用于自动构建 SlackBuilds 的工具。
> SlackBuild 源代码需要在 slapt-srcrc 文件中配置。
> 更多信息请访问：<https://github.com/jaos/slapt-src>。

- 更新可用的 SlackBuild 列表和版本：

`slapt-src --update`

- 列出所有可用的 SlackBuild：

`slapt-src --list`

- 获取、构建并安装指定的 SlackBuild：

`slapt-src --install {{slackbuild_name}}`

- 按名称或描述查找 SlackBuild：

`slapt-src --search {{search_term}}`

- 显示有关 SlackBuild 的信息：

`slapt-src --show {{slackbuild_name}}`