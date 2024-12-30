# rtcwake

> 进入系统睡眠状态，直到相对于您的 BIOS 时钟指定的唤醒时间。
> 更多信息：<https://manned.org/rtcwake>。

- 显示是否设置了闹钟：

`sudo rtcwake -m show -v`

- 挂起到内存，并在 10 秒后唤醒：

`sudo rtcwake -m mem -s {{10}}`

- 挂起到磁盘（更高的节能效果），并在 15 分钟后唤醒：

`sudo rtcwake -m disk --date +{{15}}min`

- 冻结系统（比挂起到内存更高效，但需要 Linux 内核 3.9 或更新版本），并在指定的日期和时间唤醒：

`sudo rtcwake -m freeze --date {{YYYYMMDDhhmm}}`

- 禁用之前设置的闹钟：

`sudo rtcwake -m disable`

- 执行一次干跑，以在指定时间唤醒计算机。（按 Ctrl + C 以中止）：

`sudo rtcwake -m on --date {{hh:ss}}`