# kpackagetool6

> KPackage 包管理器：安装、列出和删除 Plasma 包。
> 更多信息：<https://manned.org/kpackagetool6>。

- 列出所有可以安装的包类型：

`kpackagetool6 --list-types`

- 从目录安装包：

`kpackagetool6 --type {{package_type}} --install {{path/to/directory}}`

- 从目录更新已安装的包：

`kpackagetool6 --type {{package_type}} --upgrade {{path/to/directory}}`

- 列出已安装的等离子体小工具（使用 `--global` 列出所有用户的小工具）：

`kpackagetool6 --type Plasma/Applet --list --global`

- 按名称移除等离子体小工具：

`kpackagetool6 --type Plasma/Applet --remove "{{name}}"`
