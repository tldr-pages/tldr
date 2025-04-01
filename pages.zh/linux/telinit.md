# telinit

> 更改 SysV 运行级别。
> 由于 SysV 运行级别概念已过时，运行级别请求将被透明地转换为 systemd 单元激活请求。
> 更多信息：<https://manned.org/telinit>。

- 关机：

`telinit 0`

- 重启机器：

`telinit 6`

- 更改 SysV 运行级别：

`telinit {{2|3|4|5}}`

- 切换到救援模式：

`telinit 1`

- 重新加载守护进程配置：

`telinit q`

- 在重启/关机前不发送 wall 消息 (6/0)：

`telinit --no-wall {{value}}`