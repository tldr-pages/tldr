# picocom

> 模拟串行控制台的最小程序。
> 更多信息请访问：<https://manned.org/picocom>。

- 以指定的波特率连接到串行控制台：

`picocom {{/dev/ttyXYZ}} --baud {{baud_rate}}`

- 映射特殊字符（例如将 `LF` 映射为 `CRLF`）：

`picocom {{/dev/ttyXYZ}} --imap {{lfcrlf}}`