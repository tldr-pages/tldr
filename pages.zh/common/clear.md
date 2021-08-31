# clear

> 清空终端的屏幕。
> 更多信息：<https://manned.org/clear>.

- 清空屏幕（相当于在 Bash shell 中按 Control-L 键）：

`clear`

- 清空屏幕但保留终端的回滚缓冲区：

`clear -x`

- 指明要清空的终端类型（默认为环境变量 `TERM` 的值）：

`clear -T {{type_of_terminal}}`

- 显示 `clear` 使用的 `ncurses` 版本：

`clear -V`
