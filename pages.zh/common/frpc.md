# frpc

> frp 客户端组件，用于连接 frps 服务端并启动反向代理。
> 属于 `frp` 的一部分。
> 更多信息：<https://github.com/fatedier/frp>。

- 使用默认配置文件（当前目录下的 `frpc.ini`）启动服务：

`frpc`

- 使用新的 TOML 配置文件启动服务：

`frpc {{[-c|--config]}} {{path/to/frpc.toml}}`

- 使用指定的配置文件启动服务：

`frpc {{[-c|--config]}} {{path/to/file}}`

- 检查配置文件的有效性：

`frpc verify {{[-c|--config]}} {{path/to/file}}`

- 生成 Bash、fish、PowerShell 或 Zsh 的自动补全脚本：

`frpc completion {{bash|fish|powershell|zsh}}`

- 显示版本：

`frpc {{[-v|--version]}}`
