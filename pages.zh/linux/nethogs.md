# nethogs

> 监控每个进程的带宽使用情况。
> 更多信息：<https://github.com/raboof/nethogs>。

- 以 root 用户启动 NetHogs（默认设备为 `eth0`）：

`sudo nethogs`

- 监控特定设备的带宽：

`sudo nethogs {{device}}`

- 监控多个设备的带宽：

`sudo nethogs {{device1}} {{device2}}`

- 指定刷新频率：

`sudo nethogs -t {{seconds}}`