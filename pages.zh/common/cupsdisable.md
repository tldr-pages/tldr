# cupsdisable

> 停止打印机和打印机类。
> 注意：目标被称为打印机或打印机类。
> 另见：`cupsenable`，`cupsaccept`，`cupsreject`，`lpstat`。
> 更多信息：<https://openprinting.github.io/cups/doc/man-cupsenable.html>。

- 停止一个或多个目标：

`cupsdisable {{destination1 destination2 ...}}`

- 取消指定目标的所有作业：

`cupsdisable -c {{destination1 destination2 ...}}`