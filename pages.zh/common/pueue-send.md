# pueue 发送

> 将输入发送到任务。
> 更多信息：<https://github.com/Nukesor/pueue>。

- 将输入发送到正在运行的命令：

`pueue send {{任务ID}} "{{输入}}"`

- 向期望 y/N 的任务发送确认（例如 APT，cp）：

`pueue send {{任务ID}} {{y}}`