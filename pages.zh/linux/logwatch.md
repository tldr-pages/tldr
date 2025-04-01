# logwatch

> 汇总多个常见服务（如 apache, pam_unix, sshd 等）的日志，生成单一报告。
> 更多信息：<https://manned.org/logwatch>.

- 分析特定日期范围和详细程度的日志：

`logwatch --range {{yesterday|today|all|help}} --detail {{low|medium|others}}`

- 限制报告仅包含选定服务的信息：

`logwatch --range {{all}} --service {{apache|pam_unix|etc}}`