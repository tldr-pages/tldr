# ghostty

> 一个快速、功能丰富且跨平台的终端模拟器，使用原生平台UI和GPU加速。
> 注意：配置文件中的所有选项也可以在命令行中使用（使用 `--option=argument`）。
> 更多信息：<https://ghostty.org/docs/config/reference>。

- 打开一个新的 Ghostty 窗口（不支持 macOS）：

`ghostty`

- 在新的 Ghostty 窗口中运行特定命令（不支持 macOS）：

`ghostty -e {{command}}`

- 列出所有默认和配置的快捷键：

`ghostty +list-keybinds`

- 列出所有操作（即可以通过快捷键触发的操作）：

`ghostty +list-actions`

- 浏览一个交互式的主题列表：

`ghostty +list-themes`

- 打印默认配置（包括注释）：

`ghostty +show-config --default --docs`