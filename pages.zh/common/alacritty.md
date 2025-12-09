# alacritty

> 跨平台、GPU 加速的终端模拟器。
> 更多信息：<https://manned.org/alacritty>.

- 启动新的 Alacritty 进程并创建窗口：

`alacritty`

- 启动 Alacritty 守护进程（不创建窗口）：

`alacritty --daemon`

- 使用已运行的 Alacritty 进程创建新窗口：

`alacritty msg create-window`

- 在指定目录启动 shell（也可配合 `alacritty msg create-window` 使用）：

`alacritty --working-directory {{路径/到/目录}}`

- 执行（[e]xecute）命令到新 Alacritty 窗口（也可配合 `alacritty msg create-window` 使用）：

`alacritty -e {{命令}}`

- 使用替代配置文件（默认使用 `$XDG_CONFIG_HOME/alacritty/alacritty.toml`）：

`alacritty --config-file {{路径/到/配置.toml}}`

- 启用实时配置重载运行（也可在 `alacritty.toml` 中默认启用）：

`alacritty --live-config-reload --config-file {{路径/到/配置.toml}}`
