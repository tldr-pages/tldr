# chronyc

> 查询 Chrony NTP 守护进程。
> 更多信息：<https://chrony-project.org/doc/4.6.1/chronyc.html>.

- 以交互模式启动 `chronyc`：

`chronyc`

- 显示 Chrony 守护进程的跟踪统计信息：

`chronyc tracking`

- 打印 Chrony 当前使用的时间源：

`chronyc sources`

- 显示 Chrony 守护进程作为时间源使用的时间源的统计信息：

`chronyc sourcestats`

- 立即调整系统时钟，绕过任何平滑调整：

`chronyc makestep`

- 显示每个 NTP 源的详细信息：

`chronyc ntpdata`