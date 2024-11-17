# picocom

> 模拟串行端口的极简程序。
> 更多信息：<https://manned.org/picocom>.

- 以指定波特率连接到串行端口：

`picocom {{/dev/ttyXYZ}} --baud {{波特率}}`

- 映射特殊字符（例如：将 LF 映射为 CRLF）：

`picocom {{/dev/ttyXYZ}} --imap {{lfcrlf}}`
