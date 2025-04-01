# guix package

> 安装、升级和删除 Guix 包，或者回滚到之前的配置。
> 更多信息：<https://guix.gnu.org/manual/html_node/Invoking-guix-package.html>。

- 安装新包：

`guix package {{[-i|--install]}} {{package}}`

- 删除包：

`guix package {{[-r|--remove]}} {{package}}`

- 在包数据库中搜索正则表达式：

`guix package {{[-s|--search]}} "{{search_pattern}}"`

- 列出已安装的包：

`guix package {{[-I|--list-installed]}}`

- 列出生成版本：

`guix package {{[-l|--list-generations]}}`

- 回滚到上一个生成版本：

`guix package --roll-back`
