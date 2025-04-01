# partprobe

> 通知操作系统内核分区表的更改。
> 更多信息：<https://manned.org/partprobe>.

- 通知操作系统内核分区表的更改：

`sudo partprobe`

- 通知内核分区表的更改并显示设备及其分区的摘要：

`sudo partprobe --summary`

- 显示设备及其分区的摘要，但不通知内核：

`sudo partprobe --summary --dry-run`