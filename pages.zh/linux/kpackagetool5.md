# kpackagetool5

> KPackage 管理器：安装、列出、移除 Plasma 包。
> 更多信息：<https://manned.org/kpackagetool5>.

- 列出所有可安装的包类型：

`kpackagetool5 --list-types`

- 从目录安装包：

`kpackagetool5 --type {{package_type}} --install {{path/to/directory}}`

- 从目录更新已安装的包：

`kpackagetool5 --type {{package_type}} --upgrade {{path/to/directory}}`

- 列出已安装的桌面小工具（使用 `--global` 列出所有用户的）：

`kpackagetool5 --type Plasma/Applet --list --global`

- 按名称移除桌面小工具：

`kpackagetool5 --type Plasma/Applet --remove "{{name}}"`
