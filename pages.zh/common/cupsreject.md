# cupsreject

> 拒绝发送到打印机的打印任务。
> 注意：目标是指一个打印机或一组打印机。
> 参见：`cupsaccept`, `cupsenable`, `cupsdisable`, `lpstat`。
> 更多信息：<https://www.cups.org/doc/man-cupsaccept.html>。

- 拒绝发送到指定目标的打印任务：

`cupsreject {{destination1 destination2 ...}}`

- 指定不同的服务器：

`cupsreject -h {{server}} {{destination1 destination2 ...}}`

- 指定原因字符串（默认为"Reason Unknown"）：

`cupsreject -r {{reason}} {{destination1 destination2 ...}}`