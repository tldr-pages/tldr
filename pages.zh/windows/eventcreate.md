# eventcreate

> 在事件日志中创建自定义条目.
> 事件ID可以是1到1000之间的任意数值.

- 在日志中创建一个具有给定id（1-1000）的新事件:

`eventcreate /t {{success|error|warning|information}} /id {{id}} /d "{{消息}}"`

- 在特定事件日志中创建事件:

`eventcreate /l {{日志名}} /t {{类型}} /id {{id}} /d "{{消息}}"`

- 为新创建的事件指定来源:

`eventcreate /so {{来源名}} /t {{类型}} /id {{id}} /d "{{消息}}"`

- 在远程计算机的事件日志中创建事件:

`eventcreate /s {{主机名}} /u {{用户名}} /p {{密码}} /t {{类型}} /id {{id}} /d "{{消息"}}`
