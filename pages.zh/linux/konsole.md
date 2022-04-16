# konsole

> Konsole: KDE 终端模拟器。
> 更多信息：<https://konsole.kde.org>.

- 在特定目录中打开一个新的 Konsole：

`konsole --workdir {{path/to/directory}}`

- 运行特定命令，退出窗口后不要关闭窗口：

`konsole --noclose -e {{命令}}`

- 打开新标签页：

`konsole --new-tab`

- 在后台打开 Konsole 并在按下 Ctrl+Shift+F12（默认）时显示在最前面：

`konsole --background-mode`

- 使用紧急备冗配置文件打开 Konsole：

`konsole --fallback-profile`
