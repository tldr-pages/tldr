# wofi

> 一个基于 wlroots 的 Wayland 合成器的应用程序启动器，类似于 `rofi` 和 `dmenu`。
> 更多信息：<https://hg.sr.ht/~scoopta/wofi>.

- 显示应用程序列表：

`wofi --show drun`

- 显示所有命令的列表：

`wofi --show run`

- 将项目列表通过管道传递到 `stdin`，并在 `stdout` 中打印选中的项目：

`printf "{{Choice1\nChoice2\nChoice3}}" | wofi --dmenu`
