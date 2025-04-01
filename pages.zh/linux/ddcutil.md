# ddcutil

> 通过 DDC/CI 控制连接显示器的设置。
> 此命令需要加载内核模块 `i2c-dev`。参见：`modprobe`。
> 更多信息：<https://www.ddcutil.com>。

- 列出所有兼容的显示器：

`ddcutil detect`

- 将显示器 1 的亮度（选项 0x10）设置为 50%：

`ddcutil --display {{1}} setvcp {{10}} {{50}}`

- 将显示器 1 的对比度（选项 0x12）增加 5%：

`ddcutil -d {{1}} setvcp {{12}} {{+}} {{5}}`

- 读取显示器 1 的设置：

`ddcutil -d {{1}} getvcp {{ALL}}`
