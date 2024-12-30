# kdocker

> 轻松将应用程序停靠到系统托盘。
> 更多信息：<https://github.com/user-none/KDocker>。

- 显示一个光标，当按下左键时将窗口发送到系统托盘（按下其他鼠标按钮可取消）：

`kdocker`

- 打开一个应用程序并将其发送到系统托盘：

`kdocker {{application}}`

- 将当前聚焦的窗口发送到系统托盘：

`kdocker -f`

- 显示一个光标，当按下左键时将窗口发送到系统托盘，并使用自定义图标：

`kdocker -i {{/path/to/icon}}`

- 打开一个应用程序，将其发送到系统托盘，并在失去焦点时将其最小化：

`kdocker -l {{application}}`

- 显示版本：

`kdocker --version`