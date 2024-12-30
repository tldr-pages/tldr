# logwatch

> 在单个报告中总结许多不同服务（例如 apache、pam_unix、sshd 等）的日志。
> 更多信息：<https://manned.org/logwatch>。

- 以特定的详细级别分析一段日期的日志：

`logwatch --range {{yesterday|today|all|help}} --detail {{low|medium|others}}`

- 将报告限制为仅包括选定服务的信息：

`logwatch --range {{all}} --service {{apache|pam_unix|etc}}`