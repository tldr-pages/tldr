# systemd-notify

> 通知服务管理器有关启动完成和其他守护进程状态变化的信息。
> 此命令在 systemd 服务脚本之外无用。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/systemd-notify.html>。

- 通知 systemd 服务已完成初始化并已完全启动。应在服务准备好接受传入请求时调用：

`systemd-notify --booted`

- 向 systemd 发出信号，表示服务已准备好处理传入连接或执行其任务：

`systemd-notify --ready`

- 向 systemd 提供自定义状态消息（此信息由 `systemctl status` 显示）：

`systemd-notify --status="{{在此添加自定义状态消息...}}"`
