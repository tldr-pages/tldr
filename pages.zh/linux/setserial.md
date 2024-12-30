# setserial

> 读取和修改串口信息。
> 更多信息：<https://manned.org/setserial>。

- 打印特定串口设备的所有信息：

`setserial -a {{/dev/cuaN}}`

- 打印特定串口设备的配置摘要（在启动过程中打印时很有用）：

`setserial -b {{device}}`

- 为设备设置特定配置参数：

`sudo setserial {{device}} {{parameter}}`

- 打印设备列表的配置：

`setserial -g {{device1 device2 ...}}`