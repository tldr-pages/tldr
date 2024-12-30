# btop

> 一个资源监视器，显示有关 CPU、内存、磁盘、网络和进程的信息。
> `bpytop` 的 C++ 版本。
> 更多信息：<https://github.com/aristocratos/btop>。

- 启动 `btop`：

`btop`

- 使用指定的设置预设启动 `btop`：

`btop --preset {{0..9}}`

- 以 TTY 模式启动 `btop`，使用 16 种颜色和 TTY 友好的图形符号：

`btop --tty_on`

- 使用 256 色模式而不是 24 位颜色模式启动 `btop`：

`btop --low-color`

- 将更新率设置为 500 毫秒：

`btop --update 500`