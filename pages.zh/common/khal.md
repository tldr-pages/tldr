# khal

> 一个基于文本的日历和命令行调度应用程序。
> 更多信息：<https://lostpackets.de/khal>.

- 以交互模式启动 Khal：

`ikhal`

- 打印个人日历中未来七天的所有预定事件：

`khal list -a {{personal}} {{today}} {{7d}}`

- 打印除个人日历外，明天 10:00 的所有事件：

`khal at -d {{personal}} {{tomorrow}} {{10:00}}`

- 打印未来三个月的带有事件列表的日历：

`khal calendar`

- 将新事件添加到个人日历：

`khal new -a {{personal}} {{2020-09-08}} {{18:00}} {{18:30}} "{{看牙医}}"`
