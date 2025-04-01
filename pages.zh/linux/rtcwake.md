# rtcwake

> 将系统置于休眠状态，直到 BIOS 时钟指定的唤醒时间。
> 更多信息：<https://manned.org/rtcwake>。

- 显示是否设置了闹钟：

`sudo rtcwake {{[-m|--mode]}} show {{[-v|--verbose]}}`

- 挂起到 RAM 并在 10 秒后唤醒：

`sudo rtcwake {{[-m|--mode]}} mem {{[-s|--seconds]}} {{10}}`

- 挂起到磁盘（更高的节能效果）并在 15 分钟后唤醒：

`sudo rtcwake {{[-m|--mode]}} disk --date +{{15}}min`

- 冻结系统（比挂起到 RAM 更高效，但需要 Linux 内核 3.9 或更高版本），并在指定的日期和时间唤醒：

`sudo rtcwake {{[-m|--mode]}} freeze --date {{YYYYMMDDhhmm}}`

- 禁用之前设置的闹钟：

`sudo rtcwake {{[-m|--mode]}} disable`

- 进行一次预演以在指定时间唤醒计算机。（按 `<Ctrl c>` 中止）：

`sudo rtcwake {{[-m|--mode]}} on --date {{hh:ss}}`