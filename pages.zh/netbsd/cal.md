# cal

> 显示日历。
> 更多信息：<https://man.netbsd.org/cal.1>。

- 显示当前月份的日历：

`cal`

- 显示指定年份的日历：

`cal {{year}}`

- 显示指定年份和月份的日历：

`cal {{month}} {{year}}`

- 使用 [j]ulian 天数（从1开始，从1月1日编号）显示当前年份的完整日历：

`cal -y -j`

- [h]ighlight 今天，并显示包含指定日期的 [3] 个月：

`cal -h -3 {{month}} {{year}}`

- 显示当前年份中指定月份前 [B]efore 2 个月和后 3 [A]fter 个月：

`cal -A 3 -B 2 {{month}}`

- 显示指定月份前后的指定数量的月份 ([C]ontext)：

`cal -C {{months}} {{month}}`

- 指定一周的起始 [d]ay（0: 星期日, 1: 星期一, ..., 6: 星期六）：

`cal -d {{0..6}}`
