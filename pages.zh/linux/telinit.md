# telinit

> 更改 SysV 运行级别。
> 由于 SysV 运行级别的概念已过时，因此运行级别请求将被透明地转换为 systemd 单元激活请求。
> 更多信息：<https://manned.org/telinit>。

- 关闭机器：

`telinit 0`

- 重启机器：

`telinit 6`

- 更改 SysV 运行级别：

`telinit {{2|3|4|5}}`

- 切换到救援模式：

`telinit 1`

- 重新加载守护进程配置：

`telinit q`

- 在重启/关机（6/0）之前不发送墙消息：

`telinit --no-wall {{value}}`