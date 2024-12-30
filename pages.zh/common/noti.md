# noti

> 监控一个进程并触发横幅通知。
> 更多信息：<https://github.com/variadico/noti>。

- 当 tar 完成压缩文件时显示通知：

`noti {{tar -cjf example.tar.bz2 example/}}`

- 即使在监视命令之后放置它也显示通知：

`{{command_to_watch}}; noti`

- 通过 PID 监控一个进程，并在该 PID 消失时触发通知：

`noti -w {{process_id}}`