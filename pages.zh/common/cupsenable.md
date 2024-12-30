# cupsenable

> 启动打印机和打印机组。
> 注意：目标被称为打印机或打印机组。
> 另见：`cupsdisable`，`cupsaccept`，`cupsreject`，`lpstat`。
> 更多信息：<https://www.cups.org/doc/man-cupsenable.html>。

- 启动一个或多个目标：

`cupsenable {{destination1 destination2 ...}}`

- 恢复目标的待处理作业打印（在使用 `cupsdisable` 和 `--hold` 后使用）：

`cupsenable --release {{destination}}`

- 取消指定目标的所有作业：

`cupsenable -c {{destination1 destination2 ...}}`