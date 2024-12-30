# guix 包

> 安装、升级和移除 Guix 包，或回滚到之前的配置。
> 更多信息：<https://guix.gnu.org/manual/html_node/Invoking-guix-package.html>。

- 安装新包：

`guix package -i {{package}}`

- 移除一个包：

`guix package -r {{package}}`

- 在包数据库中搜索正则表达式：

`guix package -s "{{search_pattern}}"`

- 列出已安装的包：

`guix package -I`

- 列出版本：

`guix package -l`

- 回滚到上一个版本：

`guix package --roll-back`