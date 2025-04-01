# picocom

> 模拟串行端口的极简程序。
> 更多信息：<https://manned.org/picocom>.

- 使用默认波特率 9600 连接到串行控制台：

`sudo picocom {{/dev/ttyXYZ}}`

- 以指定波特率连接到串行控制台：

`sudo picocom {{/dev/ttyXYZ}} {{[-b|--baud]}} {{波特率}}`

- 映射特殊字符（例如：将 `LF` 映射为 `CRLF`）：

`sudo picocom {{/dev/ttyXYZ}} --imap {{lfcrlf}}`

- 退出 picocom：

`<Ctrl a><Ctrl x>`

- 显示帮助信息：

`picocom {{[-h|--help]}}`
