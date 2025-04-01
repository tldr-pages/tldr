# at

> 在未来的某个时间点执行命令一次。
> 结果将发送至用户的邮件。
> 更多信息：<https://manned.org/at>.

- 启动 `atd` 守护进程:

`systemctl start atd`

- 交互式创建命令并5分钟后执行（完成后按 `<Ctrl d>`）:

`at now + 5 minutes`

- 交互式创建命令并在特定时间执行:

`at {{hh:mm}}`

- 从 `stdin` 读取命令并在今天上午10:00执行:

`echo "{{command}}" | at 1000`

- 从指定文件中读取命令并在下周二晚上9:30执行:

`at -f {{path/to/file}} 9:30 PM Tue`

- 列出当前用户的全部排队作业（等同于 `atq`）:

`at -l`

- 查看指定的作业:

`at -c {{job_number}}`