# smartctl

> 监控磁盘健康，包括SMART数据。
> 更多信息：<https://www.smartmontools.org>。

- 显示SMART健康摘要：

`sudo smartctl --health {{/dev/sdX}}`

- 显示设备信息：

`sudo smartctl --info {{/dev/sdX}}`

- 在后台启动短时间自检：

`sudo smartctl --test short {{/dev/sdX}}`

- 显示当前/最后一次自检状态及其他SMART功能：

`sudo smartctl --capabilities {{/dev/sdX}}`

- 显示详细的SMART数据：

`sudo smartctl --all {{/dev/sdX}}`