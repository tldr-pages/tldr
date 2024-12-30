# liquidctl

> 控制液体散热器。
> 更多信息：<https://github.com/liquidctl/liquidctl>。

- 列出可用设备：

`liquidctl list`

- 初始化所有支持的设备：

`sudo liquidctl initialize all`

- 打印可用液体散热器的状态：

`liquidctl status`

- 在产品名称中匹配字符串以选择设备，并将其风扇速度设置为20°C时0%、50°C时50%和70°C时100%：

`liquidctl --match {{string}} set fan speed {{20 0 50 50 70 100}}`