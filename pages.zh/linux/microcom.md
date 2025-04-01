# microcom

> 一个极简的终端程序，用于通过串行、CAN 或 telnet 连接从控制台访问远程设备。
> 更多信息：<https://manned.org/microcom>.

- 使用指定的波特率打开串行端口：

`microcom --port {{path/to/serial_port}} --speed {{baud_rate}}`

- 与指定的主机建立 telnet 连接：

`microcom --telnet {{hostname}}:{{port}}`
