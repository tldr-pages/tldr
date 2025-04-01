# ctrlaltdel

> 控制按下 CTRL+ALT+DEL 时的行为。
> 更多信息：<https://manned.org/ctrlaltdel>。

- 获取当前设置：

`ctrlaltdel`

- 设置 CTRL+ALT+DEL 以立即重启，不进行任何准备操作：

`sudo ctrlaltdel hard`

- 设置 CTRL+ALT+DEL 以“正常”方式重启，先给进程一个退出的机会（向 PID1 发送 SIGINT）：

`sudo ctrlaltdel soft`
