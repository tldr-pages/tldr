# eww

> 在任意窗口管理器中实现自定义小部件。
> 更多信息：<https://elkowar.github.io/eww>.

- 启动守护进程：

`eww daemon`

- 打开一个小部件：

`eww -c {{path/to/source_code_directory}} open {{window_name}}`

- 关闭一个小部件：

`eww -c {{path/to/source_code_directory}} close {{window_name}}`

- 重新加载配置：

`eww reload`

- 结束守护进程：

`eww kill`

- 打印并监视日志：

`eww logs`
