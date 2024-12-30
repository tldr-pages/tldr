# gpgconf

> 修改 .gnupg 主目录。
> 更多信息：<https://www.gnupg.org/documentation/manuals/gnupg/gpgconf.html>。

- 列出所有组件：

`gpgconf --list-components`

- 列出 gpgconf 使用的目录：

`gpgconf --list-dirs`

- 列出组件的所有选项：

`gpgconf --list-options {{component}}`

- 列出程序并测试它们是否可运行：

`gpgconf --check-programs`

- 重新加载一个组件：

`gpgconf --reload {{component}}`