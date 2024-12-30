# cupsaccept

> 接受发送到目的地的作业。
> 注意：目的地指的是打印机或打印机的分类。
> 另请参见：`cupsreject`，`cupsenable`，`cupsdisable`，`lpstat`。
> 更多信息：<https://www.cups.org/doc/man-cupsaccept.html>。

- 接受发送到指定目的地的打印作业：

`cupsaccept {{destination1 destination2 ...}}`

- 指定不同的服务器：

`cupsaccept -h {{server}} {{destination1 destination2 ...}}`