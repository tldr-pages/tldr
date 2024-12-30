# at

> 在稍后的时间执行命令。
> 结果将发送到用户的邮件。
> 更多信息：<https://manned.org/at>。

- 启动 `atd` 守护进程：

`systemctl start atd`

- 交互式创建命令并在 5 分钟后执行（完成后按 `<Ctrl> + D`）：

`at now + 5 minutes`

- 交互式创建命令并在特定时间执行：

`at {{hh:mm}}`

- 在今天上午 10:00 从 `stdin` 执行命令：

`echo "{{command}}" | at 1000`

- 下周二从给定文件中执行命令：

`at -f {{path/to/file}} 9:30 PM Tue`