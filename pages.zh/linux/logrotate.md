# logrotate

> 旋转、压缩和发送系统日志。
> 更多信息：<https://manned.org/logrotate>.

- 手动触发运行：

`logrotate {{path/to/logrotate.conf}} --force`

- 使用特定命令发送报告：

`logrotate {{path/to/logrotate.conf}} --mail {{/usr/bin/mail_command}}`

- 运行时不使用状态（锁定）文件：

`logrotate {{path/to/logrotate.conf}} --state /dev/null`

- 运行并跳过状态（锁定）文件检查：

`logrotate {{path/to/logrotate.conf}} --skip-state-lock`

- 让 `logrotate` 将详细输出记录到日志文件中：

`logrotate {{path/to/logrotate.conf}} --log {{path/to/log_file}}`