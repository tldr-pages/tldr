# autossh

> 运行、监控和重启SSH连接。
> 自动重新连接以保持端口转发隧道的畅通。接受所有SSH标志。
> 更多信息：<https://www.harding.motd.ca/autossh>。

- 启动一个SSH会话，当[M]监控端口未返回数据时重启：

`autossh -M {{monitor_port}} "{{ssh_command}}"`

- 将一个[L]ocal端口转发到远程端口，在必要时重启：

`autossh -M {{monitor_port}} -L {{local_port}}:localhost:{{remote_port}} {{user}}@{{host}}`

- 在执行SSH之前将`autossh`分叉到后台，并且不打开远程shell：

`autossh -f -M {{monitor_port}} -N "{{ssh_command}}"`

- 在后台运行，没有监控端口，而是每10秒发送SSH保持活动数据包以检测故障：

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" "{{ssh_command}}"`

- 在后台运行，没有监控端口和远程shell，如果端口转发失败则退出：

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" -o ExitOnForwardFailure=yes -L {{local_port}}:localhost:{{remote_port}} {{user}}@{{host}}`

- 在后台运行，将`autossh`调试输出和SSH详细输出记录到文件：

`AUTOSSH_DEBUG=1 AUTOSSH_LOGFILE={{path/to/autossh_log_file.log}} autossh -f -M {{monitor_port}} -v -E {{path/to/ssh_log_file.log}} {{ssh_command}}`