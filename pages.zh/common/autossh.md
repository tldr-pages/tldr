# autossh

> 创建，监控或重启 SSH 连接。
> 自动重连会确保你的端口转发隧道打开。接受所有 SSH 参数。
> 更多信息：<https://manned.org/autossh>.

- 启动 SSH 会话，当监控 ([M]onitoring) 的端口无法返回数据时，自动重启：

`autossh -M {{监控_端口}} "{{ssh_命令}}"`

- 将本地 ([L]ocal) 端口转发到远程端口，必要时重启转发：

`autossh -M {{监控_端口}} -L {{本地_端口}}:localhost:{{远程_端口}} {{用户名}}@{{主机名}}`

- 在执行 SSH 命令前，将 `autossh` 切换到后台，不 ([N]ot) 启动远程 shell：

`autossh -f -M {{监控_端口}} -N "{{ssh_命令}}"`

- 后台运行，不监控端口，而是每 10 秒发送 SSH 心跳包 (SSH keep-alive packet) 来检测掉线：

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" "{{ssh_命令}}"`

- 后台运行，不监控端口，不启动远程 shell，当端口转发掉线时退出：

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" -o ExitOnForwardFailure=yes -L {{本地_端口}}:localhost:{{远程_端口}} {{用户名}}@{{主机名}}`

- 后台运行，将 `autossh` 调试输出和 SSH 详细输出写入到文件：

`AUTOSSH_DEBUG=1 AUTOSSH_LOGFILE={{路径/到/autossh_日志_文件.log}} autossh -f -M {{监控_端口}} -v -E {{路径/到/ssh_日志_文件.log}} {{ssh_命令}}`
