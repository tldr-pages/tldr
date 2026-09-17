# ghostty

> 一款快速、功能丰富、跨平台，使用原生 UI 和 GPU 加速的终端模拟器。
> 提示：所有配置文件的选项皆可在命令行使用（使用 `--option=argument`）。
> 更多信息：<https://ghostty.org/docs/config/reference>。

- 打开新的 Ghostty 窗口（不支持 macOS）：

`ghostty`

- 在新打开的 Ghostty 窗口运行指定命令（不支持 macOS）：

`ghostty -e {{命令}}`

- 列出所有默认和已配置的快捷键：

`ghostty +list-keybinds`

- 列出所有操作（即可以通过快捷键触发的操作）：

`ghostty +list-actions`

- 浏览互动式主题列表：

`ghostty +list-themes`

- 打印默认配置（包括注释）：

`ghostty +show-config --default --docs`
