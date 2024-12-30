# wmctrl

> X窗口管理器的命令行工具。
> 更多信息：<https://manned.org/wmctrl>。

- 列出所有由窗口管理器管理的窗口：

`wmctrl -l`

- 切换到第一个（部分）标题匹配的窗口：

`wmctrl -a {{window_title}}`

- 将窗口移动到当前工作区，提升其优先级并聚焦：

`wmctrl -R {{window_title}}`

- 切换到一个工作区：

`wmctrl -s {{workspace_number}}`

- 选择一个窗口并切换全屏：

`wmctrl -r {{window_title}} -b toggle,fullscreen`

- 选择一个窗口并将其移动到一个工作区：

`wmctrl -r {{window_title}} -t {{workspace_number}}`