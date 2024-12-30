# awslogs

> 从 Amazon CloudWatch 日志中查询日志组、日志流和事件。
> 更多信息：<https://github.com/jorgebastida/awslogs>。

- 列出日志组：

`awslogs groups`

- 列出指定组的现有日志流：

`awslogs streams {{/var/log/syslog}}`

- 获取指定组中 1 到 2 小时前的任何日志流的日志：

`awslogs get {{/var/log/syslog}} --start='{{2h ago}}' --end='{{1h ago}}'`

- 获取符合特定 CloudWatch Logs 过滤模式的日志：

`awslogs get {{/aws/lambda/my_lambda_group}} --filter-pattern='{{ERROR}}'`

- 监视指定组中任何日志流的日志：

`awslogs get {{/var/log/syslog}} ALL --watch`