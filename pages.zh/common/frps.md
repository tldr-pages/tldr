# frps

> 快速设置反向代理服务。
> 作为 `frp` 的一部分。
> 更多信息：<https://github.com/fatedier/frp>。

- 使用默认配置文件（假设为当前目录下的 `frps.ini`）启动服务：

`frps`

- 使用当前目录下的新 TOML 配置文件（`frps.toml` 而不是 `frps.ini`）启动服务：

`frps {{[-c|--config]}} ./frps.toml`

- 使用指定的配置文件启动服务：

`frps {{[-c|--config]}} {{path/to/file}}`

- 检查配置文件是否有效：

`frps verify {{[-c|--config]}} {{path/to/file}}`

- 打印 Bash、fish、PowerShell 或 Zsh 的自动补全设置脚本：

`frps completion {{bash|fish|powershell|zsh}}`

- 显示版本：

`frps {{[-v|--version]}}`