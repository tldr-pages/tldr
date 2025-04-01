# smartctl

> 监控磁盘健康状况，包括 SMART 数据。
> 更多信息: <https://manned.org/smartctl>。

- 显示 SMART 健康摘要：

`sudo smartctl {{[-H|--health]}} {{/dev/sdX}}`

- 显示设备信息：

`sudo smartctl {{[-i|--info]}} {{/dev/sdX}}`

- 在后台启动短/长自我检测：

`sudo smartctl {{[-t|--test]}} {{short|long}} {{/dev/sdX}}`

- 显示自我检测日志：

`sudo smartctl {{[-l|--log]}} selftest`

- 显示当前/上次自我检测状态和其他 SMART 功能：

`sudo smartctl {{[-c|--capabilities]}} {{/dev/sdX}}`

- 显示详细的 SMART 数据：

`sudo smartctl {{[-a|--all]}} {{/dev/sdX}}`
