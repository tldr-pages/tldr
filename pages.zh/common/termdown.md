# termdown

> 命令行倒计时器和秒表。
> 更多信息：<https://github.com/trehn/termdown>。

- 开始一个秒表：

`termdown`

- 开始一个1分钟30秒的倒计时：

`termdown {{1m30s}}`

- 开始一个1分钟30秒的倒计时，并在结束时闪烁终端：

`termdown {{1m30s}} --blink`

- 在倒计时上方显示标题：

`termdown {{1m30s}} --title "{{有趣的标题}}"`

- 显示当前时间：

`termdown --time`