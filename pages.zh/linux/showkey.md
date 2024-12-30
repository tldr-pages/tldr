# showkey

> 显示按下的键的键码，帮助调试与键盘相关的问题和键位重映射。
> 更多信息：<https://manned.org/showkey>。

- 以十进制查看键码：

`sudo showkey`

- 以十六进制显示扫描码：

`sudo showkey {{-s|--scancodes}}`

- 以十进制显示键码（默认）：

`sudo showkey {{-k|--keycodes}}`

- 以ASCII、十进制和十六进制显示键码：

`sudo showkey {{-a|--ascii}}`

- 退出程序：

`Ctrl + d`