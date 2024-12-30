# vcgencmd

> 打印树莓派的系统信息。
> 更多信息：<https://www.raspberrypi.com/documentation/computers/os.html#vcgencmd>。

- 列出所有可用命令：

`vcgencmd commands`

- 打印当前CPU温度：

`vcgencmd measure_temp`

- 打印当前电压：

`vcgencmd measure_volts`

- 以位模式打印系统的节流状态：

`vcgencmd get_throttled`

- 打印引导加载程序配置（仅适用于树莓派4型号）：

`vcgencmd bootloader_config`

- 显示帮助信息：

`vcgencmd --help`