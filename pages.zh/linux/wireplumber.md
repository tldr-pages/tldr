# wireplumber

> PipeWire 的模块化会话/策略管理器，以及基于 GObject 的高级库，用于封装 PipeWire 的 API。
> 参见：`wpctl`，`pipewire`。
> 更多信息：<https://pipewire.pages.freedesktop.org/wireplumber/>。

- 让 WirePlumber 立即与用户会话一起启动（适用于 systemd 系统）：

`systemctl --user --now enable wireplumber`

- 在启动 `pipewire` 之后运行 WirePlumber（适用于非 systemd 系统）：

`wireplumber`

- 指定不同的上下文配置文件：

`wireplumber --config-file {{path/to/file}}`

- 显示帮助：

`wireplumber --help`

- 显示版本：

`wireplumber --version`