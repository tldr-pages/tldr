# repquota

> 显示文件系统中现有文件配额的摘要。
> 更多信息：<https://manned.org/repquota>.

- 报告所有正在使用的配额统计信息：

`sudo repquota -all`

- 报告所有用户的配额统计信息，即使他们没有使用配额：

`sudo repquota -v {{filesystem}}`

- 仅报告用户的配额：

`repquota --user {{filesystem}}`

- 仅报告组的配额：

`sudo repquota --group {{filesystem}}`

- 以人类可读的格式报告已使用的配额和限制：

`sudo repquota --human-readable {{filesystem}}`

- 以人类可读的格式报告所有用户和组的配额：

`sudo repquota -augs`
