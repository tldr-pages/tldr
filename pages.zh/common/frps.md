# frps

> 快速建立反向代理服务。
> 属于 `frp` 的一部分。
> 更多信息： <https://github.com/fatedier/frp>.

- 使用默认配置文件（当前目录下的 `frps.ini`）启动服务：

`frps`

- 使用新的 TOML 配置文件启动服务：

`frps {{[-c|--config]}} {{path/to/frps.toml}}`

- 使用指定的配置文件启动服务：

`frps {{[-c|--config]}} {{path/to/file}}`

- 检查配置文件的有效性：

`frps verify {{[-c|--config]}} {{path/to/file}}`

- 生成 Bash、fish、PowerShell 或 Zsh 的自动补全脚本：

`frps completion {{bash|fish|powershell|zsh}}`

- 显示版本号：

`frps {{[-v|--version]}}`
