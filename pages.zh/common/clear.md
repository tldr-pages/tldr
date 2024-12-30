# 清屏

> 清除终端屏幕。
> 更多信息：<https://manned.org/clear>。

- 清除屏幕：

`clear`

- 清除屏幕但保留终端的滚动缓冲区（相当于在 Bash 中按 Ctrl + L）：

`clear -x`

- 指定要清除的终端类型（默认为环境变量 `TERM` 的值）：

`clear -T {{终端类型}}`

- 显示 `clear` 使用的 `ncurses` 版本：

`clear -V`