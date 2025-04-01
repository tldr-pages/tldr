# xxh

> 将包含所有自定义设置的 shell 通过 SSH 会话带到目标机器。
> 注意：xxh 不会在目标机器的系统目录中安装任何内容；移除 `~/.xxh` 将清除目标机器上所有 xxh 的痕迹。
> 更多信息：<https://github.com/xxh/xxh>.

- 连接到主机并运行当前 shell：

`xxh "{{host}}"`

- 在目标机器上安装当前 shell，无需提示：

`xxh "{{host}}" ++install`

- 在目标机器上运行指定的 shell：

`xxh "{{host}}" ++shell {{xonsh|zsh|fish|bash|osquery}}`

- 在目标机器上使用特定的 xxh 配置目录：

`xxh "{{host}}" ++host-xxh-home {{~/.xxh}}`

- 在主机上使用指定的配置文件：

`xxh "{{host}}" ++xxh-config {{~/.config/xxh/config.xxhc}}`

- 指定用于 SSH 连接的密码：

`xxh "{{host}}" ++password "{{password}}"`

- 在目标机器上安装 xxh 包：

`xxh "{{host}}" ++install-xxh-packages {{package}}`

- 为目标机器上的 shell 进程设置环境变量：

`xxh "{{host}}" ++env {{name}}={{value}}`
