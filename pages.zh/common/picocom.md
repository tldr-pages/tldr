# picocom

> 模拟串行控制台的极简程序。
> 更多信息：<https://manned.org/picocom>.

- 以指定波特率连接到串行控制台：

`picocom {{/dev/ttyXYZ}} --baud {{baud_rate}}`

- 映射特殊字符（例如：将 LF 映射为 CRLF）：

`picocom {{/dev/ttyXYZ}} --imap {{lfcrlf}}`
