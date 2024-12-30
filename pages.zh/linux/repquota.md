# repquota

> 显示文件系统现有文件配额的摘要。
> 更多信息：<https://manned.org/repquota>。

- 报告所有正在使用的配额的统计信息：

`sudo repquota -all`

- 报告所有用户的配额统计信息，即使这些用户没有使用他们的配额：

`sudo repquota -v {{文件系统}}`

- 仅报告用户的配额：

`repquota --user {{文件系统}}`

- 仅报告组的配额：

`sudo repquota --group {{文件系统}}`

- 以人类可读的格式报告已使用的配额和限制：

`sudo repquota --human-readable {{文件系统}}`

- 以人类可读的格式报告用户和组的所有配额：

`sudo repquota -augs`