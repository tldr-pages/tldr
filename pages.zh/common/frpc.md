# frpc

> 连接到 `frps` 服务器以开始在当前主机上代理连接。
> 是 `frp` 的一部分。
> 更多信息：<https://github.com/fatedier/frp>。

- 启动服务，使用默认配置文件（假定为当前目录中的 `frps.ini`）：

`frpc`

- 启动服务，使用更新的 TOML 配置文件（在当前目录中使用 `frps.toml` 而不是 `frps.ini`）：

`frpc {{-c|--config}} ./frps.toml`

- 启动服务，使用特定配置文件：

`frpc {{-c|--config}} {{path/to/file}}`

- 检查配置文件是否有效：

`frpc verify {{-c|--config}} {{path/to/file}}`

- 打印 Bash、fish、PowerShell 或 Zsh 的自动补全设置脚本：

`frpc completion {{bash|fish|powershell|zsh}}`

- 显示版本：

`frpc {{-v|--version}}`