# startx

> `xinit` 的前端工具，为运行 X Window 系统的单个会话提供友好的用户界面。
> 更多信息：<https://x.org/releases/X11R7.5/doc/man/man1/startx.1.html>.

- 启动一个 X 会话：

`startx`

- 使用预定义的深度值启动 X 会话：

`startx -- -depth {{value}}`

- 使用预定义的 dpi 值启动 X 会话：

`startx -- -dpi {{value}}`

- 覆盖 `.xinitrc` 文件中的设置并启动新的 X 会话：

`startx /{{path/to/window_manager_or_desktop_environment}}`