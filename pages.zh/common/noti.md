# noti

> 监视进程并在进程完成后触发通知。
> 更多信息：<https://github.com/variadico/noti>.

- 当 tar 完成文件压缩时显示通知：

`noti {{tar -cjf example.tar.bz2 example/}}`

- 即使将通知命令放在要监视的命令之后，也能显示通知：

`{{command_to_watch}}; noti`

- 通过 PID 监视进程，并在 PID 消失时触发通知：

`noti -w {{process_id}}`
