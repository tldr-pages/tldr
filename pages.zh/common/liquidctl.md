# liquidctl

> 控制液冷设备。
> 更多信息：<https://github.com/liquidctl/liquidctl>.

- 列出可用设备：

`liquidctl list`

- 初始化所有支持的设备：

`sudo liquidctl initialize all`

- 打印可用液冷设备的状态：

`liquidctl status`

- 在产品名称中匹配字符串以选择设备，并将其风扇速度设置为 20°C 时 0%，50°C 时 50%，70°C 时 100%：

`liquidctl --match {{string}} set fan speed {{20 0 50 50 70 100}}`