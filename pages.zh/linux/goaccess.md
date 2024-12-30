# goaccess

> 一个开源的实时网页日志分析器。
> 更多信息：<https://goaccess.io>。

- 在交互模式下分析一个或多个日志文件：

`goaccess {{path/to/logfile1 path/to/file2 ...}}`

- 使用特定的日志格式（或预定义的格式，如“combined”）：

`goaccess {{path/to/logfile}} --log-format={{format}}`

- 从 `stdin` 分析日志：

`tail -f {{path/to/logfile}} | goaccess -`

- 分析日志并实时写入 HTML 文件：

`goaccess {{path/to/logfile}} --output {{path/to/file.html}} --real-time-html`