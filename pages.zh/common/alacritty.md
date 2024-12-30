# alacritty

> 跨平台，GPU 加速的终端仿真器。
> 更多信息：<https://github.com/alacritty/alacritty>。

- 打开一个新的 Alacritty 窗口：

`alacritty`

- 在特定目录下运行：

`alacritty --working-directory {{path/to/directory}}`

- 在新的 Alacritty 窗口中[e]xecute一个命令：

`alacritty -e {{command}}`

- 使用备用配置文件（默认使用 `$XDG_CONFIG_HOME/alacritty/alacritty.toml`）：

`alacritty --config-file {{path/to/config.toml}}`

- 运行时启用实时配置重载（也可以在 `alacritty.toml` 中默认启用）：

`alacritty --live-config-reload --config-file {{path/to/config.toml}}`