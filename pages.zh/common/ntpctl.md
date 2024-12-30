# ntpctl

> 显示关于正在运行的 OpenNTPD 实例的信息。
> 更多信息: <https://man.openbsd.org/ntpctl>。

- 显示所有数据：

`ntpctl -s {{a|all}}`

- 显示每个对等体的信息：

`ntpctl -s {{p|peers}}`

- 显示对等体和传感器的状态，以及系统时钟是否已同步：

`ntpctl -s {{s|status}}`

- 显示每个传感器的信息：

`ntpctl -s {{S|Sensors}}`