# setserial

> 读取和修改串行端口信息。
> 更多信息：<https://manned.org/setserial>.

- 打印特定串行设备的所有信息：

`setserial -a {{/dev/cuaN}}`

- 打印特定串行设备的配置摘要（在启动过程中打印非常有用）：

`setserial -b {{device}}`

- 设置特定设备的某一配置参数：

`sudo setserial {{device}} {{parameter}}`

- 打印一系列设备的配置：

`setserial -g {{device1 device2 ...}}`
