# wmctrl

> X Window Manager 的命令行接口。
> 更多信息：<https://manned.org/wmctrl>.

- 列出窗口管理器管理的所有窗口：

`wmctrl -l`

- 切换到部分标题匹配的第一个窗口：

`wmctrl -a {{window_title}}`

- 将窗口移动到当前工作区，并提升和聚焦该窗口：

`wmctrl -R {{window_title}}`

- 切换到指定的工作区：

`wmctrl -s {{workspace_number}}`

- 选择一个窗口并切换全屏模式：

`wmctrl -r {{window_title}} -b toggle,fullscreen`

- 选择一个窗口并将其移动到指定的工作区：

`wmctrl -r {{window_title}} -t {{workspace_number}}`