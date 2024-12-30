# konsole

> KDE 的终端模拟器。
> 更多信息：<https://docs.kde.org/stable5/zh/konsole/konsole/command-line-options.html>。

- 在特定目录中打开终端：

`konsole --workdir {{path/to/directory}}`

- [e]xecute 一个特定命令，并在命令执行完毕后不关闭窗口：

`konsole --noclose -e "{{command}}"`

- 打开一个新标签：

`konsole --new-tab`

- 在后台打开终端，并在按下 `Ctrl+Shift+F12` 时将其带到前台：

`konsole --background-mode`