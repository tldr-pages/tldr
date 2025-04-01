# cal

> 显示一个带有当前日期高亮的日历。
> 更多信息：<https://man.freebsd.org/cgi/man.cgi?cal>。

- 显示当前月份的日历：

`cal`

- 显示特定年份的日历：

`cal {{year}}`

- 显示特定年份和月份的日历：

`cal {{month}} {{year}}`

- 显示当前年份的完整日历：

`cal -y`

- 不高亮今天，并显示 [3] 个月的时间范围：

`cal -h -3 {{month}} {{year}}`

- 显示当前年份中特定 [m] 月份前 [B]2 个月和后 [A]3 个月的日历：

`cal -A 3 -B 2 {{month}}`

- 显示 [j]ulian 日（从 1 开始，从 1 月 1 日开始编号）：

`cal -j`
