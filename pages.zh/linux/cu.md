# cu

> 呼叫另一个系统并充当拨号/串行终端，或者执行文件传输而不进行错误检查。
> 更多信息：<https://manned.org/cu>。

- 打开指定的串行端口：

`sudo cu --line {{/dev/ttyUSB0}}`

- 以指定的波特率打开指定的串行端口：

`sudo cu --line {{/dev/ttyUSB0}} --speed {{115200}}`

- 以指定的波特率打开指定的串行端口并在本地回显字符（半双工模式）：

`sudo cu --line {{/dev/ttyUSB0}} --speed {{115200}} --halfduplex`

- 以指定的波特率、奇偶校验，并且不使用硬件或软件流控制打开指定的串行端口：

`sudo cu --line {{/dev/ttyUSB0}} --speed {{115200}} --parity={{even|odd|none}} --nortscts --nostop`

- 在连接时退出 `cu` 会话：

`~.`