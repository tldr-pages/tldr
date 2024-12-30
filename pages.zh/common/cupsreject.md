# cupsreject

> 拒绝发送到打印机的作业。
> 注意：目标被称为打印机或打印机类别。
> 另见：`cupsaccept`、`cupsenable`、`cupsdisable`、`lpstat`。
> 更多信息：<https://www.cups.org/doc/man-cupsaccept.html>。

- 拒绝发送到指定目标的打印作业：

`cupsreject {{destination1 destination2 ...}}`

- 指定不同的服务器：

`cupsreject -h {{server}} {{destination1 destination2 ...}}`

- 指定一个原因字符串（默认是“原因未知”）：

`cupsreject -r {{reason}} {{destination1 destination2 ...}}`