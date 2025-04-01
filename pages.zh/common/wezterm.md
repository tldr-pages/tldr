# wezterm

> Wez的终端模拟器 - 一个强大的跨平台终端模拟器和多路复用器。
> 更多信息：<https://wezterm.org/cli/general>.

- 启动一个新 Wezterm 进程并创建一个窗口：

`wezterm`

- 建立 `ssh` 会话：

`wezterm ssh {{user}}@{{host}}:{{port}}`

- 连接到多路复用器（`wezterm-mux-server`）：

`wezterm connect {{domain_name}}`

- 将图像输出到终端：

`wezterm imgcat {{path/to/image}}`

- 记录一个终端会话为 asciicat（默认记录保存在 `/tmp`）：

`wezterm record`

- 重放 asciicat 终端会话：

`wezterm replay {{path/to/cast_file}}`

- 指定要使用的配置文件（覆盖正常的配置文件解析）：

`wezterm --config-file {{path/to/config_file}}`

- 显示帮助：

`wezterm help`