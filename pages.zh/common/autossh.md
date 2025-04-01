# autossh

> 运行、监视和重启 SSH 连接。
> 自动重新连接以保持端口转发隧道的连接。接受所有 SSH 标志。
> 更多信息：<https://manned.org/autossh>.

- 启动一个 SSH 会话，当 [M]onitoring 端口无法返回数据时重启：

`autossh -M {{monitor_port}} "{{ssh_command}}"`

- 将 [L]ocal 端口转发到远程端口，必要时重启：

`autossh -M {{monitor_port}} -L {{local_port}}:localhost:{{remote_port}} {{user}}@{{host}}`

- 在执行 SSH 之前将 `autossh` 叉到后台，并且不打开远程 shell：

`autossh -f -M {{monitor_port}} -N "{{ssh_command}}"`

- 在后台运行，不使用监控端口，而是每 10 秒发送 SSH 保持活动包以检测失败：

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" "{{ssh_command}}"`

- 在后台运行，不使用监控端口和远程 shell，如果端口转发失败则退出：

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" -o ExitOnForwardFailure=yes -L {{local_port}}:localhost:{{remote_port}} {{user}}@{{host}}`

- 在后台运行，记录 `autossh` 调试输出和 SSH 详细输出到文件：

`AUTOSSH_DEBUG=1 AUTOSSH_LOGFILE={{path/to/autossh_log_file.log}} autossh -f -M {{monitor_port}} -v -E {{path/to/ssh_log_file.log}} {{ssh_command}}`
