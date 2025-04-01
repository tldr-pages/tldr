# xbps-query

> 用于查询软件包和仓库信息的 XBPS 工具。
> 另请参阅：`xbps`。
> 更多信息：<https://manned.org/xbps-query.1>。

- 使用正则表达式或关键字搜索远程仓库中的软件包（如果省略 `--regex`，则使用关键字搜索）：

`xbps-query --search {{正则表达式|关键字}} --repository --regex`

- 显示已安装软件包的信息：

`xbps-query --show {{软件包}}`

- 显示远程仓库中软件包的信息：

`xbps-query --show {{软件包}} --repository`

- 列出在软件包数据库中注册的所有软件包：

`xbps-query --list-pkgs`

- 列出显式安装的软件包（即不是作为依赖项自动安装的）：

`xbps-query --list-manual-pkgs`
