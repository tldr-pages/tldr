# cu

> 调用另一个系统并作为拨入/串行终端，或在没有错误检查的情况下传输文件。
> 更多信息：<https://manned.org/cu>.

- 打开指定的串行端口：

`sudo cu {{[-l|--line]}} {{/dev/ttyXYZ}}`

- 以指定波特率打开指定的串行端口：

`sudo cu {{[-l|--line]}} {{/dev/ttyXYZ}} {{[-s|--speed]}} {{115200}}`

- 以指定波特率打开指定的串行端口，并在本地回显字符（半双工模式）：

`sudo cu {{[-l|--line]}} {{/dev/ttyXYZ}} {{[-s|--speed]}} {{115200}} {{[-h|--halfduplex]}}`

- 以指定波特率、奇偶校验、以及不使用硬件或软件流控制的方式打开指定的串行端口：

`sudo cu {{[-l|--line]}} {{/dev/ttyXYZ}} {{[-s|--speed]}} {{115200}} --parity={{even|odd|none}} {{[-f|--nortscts]}} --nostop`

- 在连接中退出 `cu` 会话：

`<Enter><~><.>`

- 显示帮助：

`cu --help`
