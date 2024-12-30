# khal

> 一个基于文本的日历和调度应用程序，适用于命令行。
> 更多信息：<https://lostpackets.de/khal>。

- 在交互模式下启动Khal：

`ikhal`

- 打印个人日历中接下来七天内安排的所有事件：

`khal list -a {{personal}} {{today}} {{7d}}`

- 打印明天上午10:00不在个人日历中的所有安排的事件：

`khal at -d {{personal}} {{tomorrow}} {{10:00}}`

- 打印接下来三个月的事件日历：

`khal calendar`

- 向个人日历添加新事件：

`khal new -a {{personal}} {{2020-09-08}} {{18:00}} {{18:30}} "{{牙医预约}}"`