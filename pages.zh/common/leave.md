# 离开

> 设置一个提醒，提醒你何时离开。
> 要删除提醒，请使用 `kill $(pidof leave)`。
> 更多信息：<https://www.freebsd.org/cgi/man.cgi?query=leave>。

- 在指定时间设置提醒：

`leave {{time_to_leave}}`

- 设置中午离开的提醒：

`leave {{1200}}`

- 设置在特定时间段后离开的提醒：

`leave +{{amount_of_time}}`

- 设置在4小时4分钟后离开的提醒：

`leave +{{0404}}`