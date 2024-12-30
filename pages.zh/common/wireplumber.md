# WirePlumber

> 一个模块化的会话/策略管理器，用于 PipeWire，以及一个基于 GObject 的高级库，用于封装 PipeWire 的 API。
> 另请参见：`wpctl`，`pipewire`。
> 更多信息：<https://pipewire.pages.freedesktop.org/wireplumber/>.

- 使 WirePlumber 在用户会话中立即启动（对于 systemd 系统）：

`systemctl --user --now enable wireplumber`

- 在 `pipewire` 启动后运行 WirePlumber（对于非 systemd 系统）：

`wireplumber`

- 指定不同的上下文配置文件：

`wireplumber --config-file {{path/to/file}}`

- 显示帮助信息：

`wireplumber --help`

- 显示版本：

`wireplumber --version`