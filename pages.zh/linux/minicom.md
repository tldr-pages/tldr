# minicom

> 与设备的串行接口进行通信。
> 更多信息：<https://manned.org/minicom>.

- 打开给定的串行端口：

`sudo minicom {{[-D|--device]}} {{/dev/ttyUSB0}}`

- 以给定的波特率打开给定的串行端口：

`sudo minicom {{[-D|--device]}} {{/dev/ttyUSB0}} {{[-b|--baudrate]}} {{115200}}`

- 在与给定串行端口通信前进入配置菜单：

`sudo minicom {{[-D|--device]}} {{/dev/ttyUSB0}} {{[-s|--setup]}}`
