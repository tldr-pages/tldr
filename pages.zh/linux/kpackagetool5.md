# kpackagetool5

> KPackage 管理器：安装、列出、删除 Plasma 包。
> 更多信息：<https://techbase.kde.org/Development/Tutorials/Plasma5/QML2/GettingStarted#Kpackagetool5>。

- 列出所有已知的可安装包类型：

`kpackagetool5 --list-types`

- 从目录安装包：

`kpackagetool5 --type {{package_type}} --install {{path/to/directory}}`

- 从目录更新已安装的包：

`kpackagetool5 --type {{package_type}} --upgrade {{path/to/directory}}`

- 列出已安装的 plasmoids (--global 为所有用户)：

`kpackagetool5 --type Plasma/Applet --list --global`

- 通过名称删除一个 plasmoid：

`kpackagetool5 --type Plasma/Applet --remove "{{name}}"`