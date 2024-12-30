# xxh

> 通过SSH会话带上您所有的自定义设置。
> 注意：xxh不会在目标机器的系统目录中安装任何东西；删除`~/.xxh`将清除目标机器上所有xxh的痕迹。
> 更多信息：<https://github.com/xxh/xxh>。

- 连接到主机并运行当前的shell：

`xxh "{{host}}"`

- 在目标机器上安装当前的shell而不提示：

`xxh "{{host}}" ++install`

- 在目标机器上运行指定的shell：

`xxh "{{host}}" ++shell {{xonsh|zsh|fish|bash|osquery}}`

- 在目标机器上使用特定的xxh配置目录：

`xxh "{{host}}" ++host-xxh-home {{~/.xxh}}`

- 在主机上使用指定的配置文件：

`xxh "{{host}}" ++xxh-config {{~/.config/xxh/config.xxhc}}`

- 指定用于SSH连接的密码：

`xxh "{{host}}" ++password "{{password}}"`

- 在目标机器上安装xxh包：

`xxh "{{host}}" ++install-xxh-packages {{package}}`

- 为目标机器上的shell进程设置环境变量：

`xxh "{{host}}" ++env {{name}}={{value}}`