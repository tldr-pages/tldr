# frps

> 快速设置反向代理服务。
> 属于 `frp` 的一部分。
> 更多信息：<https://github.com/fatedier/frp>。

- 启动服务，使用默认配置文件（假设为当前目录中的 `frps.ini`）：

`frps`

- 启动服务，使用更新的 TOML 配置文件（在当前目录中使用 `frps.toml` 而不是 `frps.ini`）：

`frps {{-c|--config}} ./frps.toml`

- 启动服务，使用指定的配置文件：

`frps {{-c|--config}} {{path/to/file}}`

- 检查配置文件是否有效：

`frps verify {{-c|--config}} {{path/to/file}}`

- 打印 Bash、fish、PowerShell 或 Zsh 的自动补全设置脚本：

`frps completion {{bash|fish|powershell|zsh}}`

- 显示版本：

`frps {{-v|--version}}`