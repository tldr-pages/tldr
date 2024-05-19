# alacritty

> 跨平台，GPU 加速的终端模拟器。
> 更多信息：<https://github.com/alacritty/alacritty>.

- 打开一个新的 Alacritty 窗口：

`alacritty`

- 运行在指定目录中：

`alacritty --working-directory {{路径}}`

- 在新的 Alacritty 窗口中运行命令：

`alacritty -e {{命令}}`

- 指定备用配置文件（默认在 `$XDG_CONFIG_HOME/alacritty/alacritty.toml`）：

`alacritty --config-file {{路径/config.toml}}`

- 在启用实时配置重新加载的情况下运行（默认情况下也可以在 `alacritty.toml` 中启用）：

`alacritty --live-config-reload --config-file {{路径/config.toml}}`
