# awslogs

> 查询 Amazon CloudWatch 日志中的日志组、日志流和日志事件。
> 更多信息：<https://github.com/jorgebastida/awslogs>。

- 列出日志组：

`awslogs groups`

- 列出指定日志组中的现有日志流：

`awslogs streams {{/var/log/syslog}}`

- 获取指定日志组中在1到2小时之间的任意日志流的日志：

`awslogs get {{/var/log/syslog}} --start='{{2h ago}}' --end='{{1h ago}}'`

- 获取与特定 CloudWatch 日志过滤模式匹配的日志：

`awslogs get {{/aws/lambda/my_lambda_group}} --filter-pattern='{{ERROR}}'`

- 监视指定日志组中任意日志流的日志：

`awslogs get {{/var/log/syslog}} ALL --watch`