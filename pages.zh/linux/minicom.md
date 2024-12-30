# minicom

> 与设备的串行接口进行通信。
> 更多信息：<https://manned.org/minicom>。

- 打开指定的串行端口：

`sudo minicom --device {{/dev/ttyUSB0}}`

- 以指定的波特率打开指定的串行端口：

`sudo minicom --device {{/dev/ttyUSB0}} --baudrate {{115200}}`

- 在与指定的串行端口通信之前进入配置菜单：

`sudo minicom --device {{/dev/ttyUSB0}} --setup`