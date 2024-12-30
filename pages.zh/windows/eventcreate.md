# eventcreate

> 在事件日志中创建自定义条目。
> 事件 ID 可以是 1 到 1000 之间的任意数字。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/eventcreate>。

- 在日志中创建具有给定 ID（1-1000）的新事件：

`eventcreate /t {{success|error|warning|information}} /id {{id}} /d "{{message}}"`

- 在特定事件日志中创建事件：

`eventcreate /l {{log_name}} /t {{type}} /id {{id}} /d "{{message}}"`

- 创建具有特定源的事件：

`eventcreate /so {{source_name}} /t {{type}} /id {{id}} /d "{{message}}"`

- 在远程计算机的事件日志中创建事件：

`eventcreate /s {{hostname}} /u {{username}} /p {{password}} /t {{type}} /id {{id}} /d "{{message}} "`