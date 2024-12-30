# pio 设备

> 管理和监控 PlatformIO 设备。
> 更多信息：<https://docs.platformio.org/en/latest/core/userguide/device/>.

- 列出所有可用的串口：

`pio device list`

- 列出所有可用的逻辑设备：

`pio device list --logical`

- 启动交互式设备监视器：

`pio device monitor`

- 启动交互式设备监视器并监听特定端口：

`pio device monitor --port {{/dev/ttyUSBX}}`

- 启动交互式设备监视器并设置特定波特率（默认为 9600）：

`pio device monitor --baud {{57600}}`

- 启动交互式设备监视器并设置特定的行结束符（默认为 `CRLF`）：

`pio device monitor --eol {{CRLF|CR|LF}}`

- 进入交互式设备监视器的菜单：

`<Ctrl> + T`