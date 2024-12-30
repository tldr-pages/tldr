# ctrlaltdel

> 控制按下 CTRL+ALT+DEL 时发生的事情的工具。
> 更多信息：<https://manned.org/ctrlaltdel>。

- 获取当前设置：

`ctrlaltdel`

- 设置 CTRL+ALT+DEL 立即重启，无需任何准备：

`sudo ctrlaltdel hard`

- 设置 CTRL+ALT+DEL 正常重启，给进程一个先退出的机会（向 PID1 发送 SIGINT）：

`sudo ctrlaltdel soft`