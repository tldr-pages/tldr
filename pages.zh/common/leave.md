# leave

> 设置一个提醒，提示何时该离开。
> 若要移除提醒，使用 `kill $(pidof leave)`。
> 更多信息：<https://www.freebsd.org/cgi/man.cgi?query=leave>.

- 在指定时间设置提醒：

`leave {{time_to_leave}}`

- 在中午时设置提醒：

`leave {{1200}}`

- 在特定时间后设置提醒：

`leave +{{amount_of_time}}`

- 在4小时4分钟后设置提醒：

`leave +{{0404}}`
