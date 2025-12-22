# awslogs

> 从 Amazon CloudWatch Logs 中查询日志组、日志流和事件。
> 更多信息：<https://github.com/jorgebastida/awslogs#options>.

- 列出日志组：

`awslogs groups`

- 列出指定日志组中已有的日志流：

`awslogs streams {{/路径/到/syslog}}`

- 获取指定日志组中 1 到 2 小时前任意日志流的日志：

`awslogs get {{/路径/到/syslog}} {{[-s|--start]}} '{{2 小时前}}' {{[-e|--end]}} '{{1 小时前}}'`

- 获取匹配特定 CloudWatch Logs 过滤模式的日志：

`awslogs get {{/aws/lambda/my_lambda_group}} --filter-pattern '{{ERROR}}'`

- 监视指定日志组中任意日志流的日志：

`awslogs get {{/路径/到/syslog}} ALL --watch`
