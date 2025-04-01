# slapt-src

> 用于自动构建 SlackBuild 的工具。
> SlackBuild 源需要在 slapt-srcrc 文件中进行配置。
> 更多信息：<https://github.com/jaos/slapt-src>。

- 更新可用的 SlackBuild 列表和版本：

`slapt-src --update`

- 列出所有可用的 SlackBuild：

`slapt-src --list`

- 获取、构建并安装指定的 SlackBuild：

`slapt-src --install {{slackbuild_name}}`

- 通过名称或描述查找 SlackBuild：

`slapt-src --search {{search_term}}`

- 显示关于某个 SlackBuild 的信息：

`slapt-src --show {{slackbuild_name}}`