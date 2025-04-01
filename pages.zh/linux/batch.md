# batch

> 在系统负载允许时稍后执行命令。
> 结果将发送到用户的邮件中。
> 参见：`at`, `atq`, `atrm` `mail`。
> 更多信息：<https://manned.org/batch>.

- 启动 `atd` 守护进程：

`systemctl start atd`

- 从 `stdin` 执行命令（完成后按 `<Ctrl d>`）：

`batch`

- 从 `stdin` 执行一个命令：

`echo "{{./make_db_backup.sh}}" | batch`
