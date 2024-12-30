# startx

> `xinit` 的前端，提供了一个良好的用户界面，用于运行单个 X 窗口系统会话。
> 更多信息：<https://x.org/releases/X11R7.5/doc/man/man1/startx.1.html>。

- 启动一个 X 会话：

`startx`

- 以预定义的深度值启动 X 会话：

`startx -- -depth {{value}}`

- 以预定义的 dpi 值启动 X 会话：

`startx -- -dpi {{value}}`

- 覆盖 `.xinitrc` 文件中的设置并启动新的 X 会话：

`startx /{{path/to/window_manager_or_desktop_environment}}`