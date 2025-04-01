# xfce4-terminal

> XFCE4 终端模拟器。
> 更多信息：<https://docs.xfce.org/apps/xfce4-terminal/start>.

- 打开一个新的终端窗口：

`xfce4-terminal`

- 设置初始标题：

`xfce4-terminal --initial-title "{{initial_title}}"`

- 在当前终端窗口中打开一个新的标签页：

`xfce4-terminal --tab`

- 在新的终端窗口中执行命令：

`xfce4-terminal --command "{{command_with_args}}"`

- 命令执行完成后保持终端窗口打开：

`xfce4-terminal --command "{{command_with_args}}" --hold`

- 打开多个新标签页，并在每个标签页中执行命令：

`xfce4-terminal --tab --command "{{command1}}" --tab --command "{{command2}}"`
