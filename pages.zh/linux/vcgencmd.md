# vcgencmd

> 打印 Raspberry Pi 的系统信息。
> 更多信息：<https://www.raspberrypi.com/documentation/computers/os.html#vcgencmd>。

- 列出所有可用的命令：

`vcgencmd commands`

- 打印当前的 CPU 温度：

`vcgencmd measure_temp`

- 打印当前的电压：

`vcgencmd measure_volts`

- 以位模式打印系统的节流状态：

`vcgencmd get_throttled`

- 打印引导加载程序配置（仅适用于 Raspberry Pi 4 型号）：

`vcgencmd bootloader_config`

- 显示帮助：

`vcgencmd --help`
