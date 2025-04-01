# frpc

> 连接到 `frps` 服务器以在当前主机上开始代理连接。
> 属于 `frp`。
> 更多信息：<https://github.com/fatedier/frp>。

- 使用默认配置文件（假定为当前目录下的 `frps.ini`）启动服务：

`frpc`

- 使用当前目录中的新 TOML 配置文件（`frps.toml` 而不是 `frps.ini`）启动服务：

`frpc {{[-c|--config]}} ./frps.toml`

- 使用指定的配置文件启动服务：

`frpc {{[-c|--config]}} {{path/to/file}}`

- 检查配置文件是否有效：

`frpc verify {{[-c|--config]}} {{path/to/file}}`

- 打印 Bash、fish、PowerShell 或 Zsh 的自动补全设置脚本：

`frpc completion {{bash|fish|powershell|zsh}}`

- 显示版本：

`frpc {{[-v|--version]}}`