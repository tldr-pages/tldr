# microcom

> 一款极简的终端程序，用于通过串口、CAN或telnet连接从控制台访问远程设备。
> 更多信息：<https://manned.org/microcom>。

- 使用指定的波特率打开串口：

`microcom --port {{path/to/serial_port}} --speed {{baud_rate}}`

- 建立与指定主机的telnet连接：

`microcom --telnet {{hostname}}:{{port}}`