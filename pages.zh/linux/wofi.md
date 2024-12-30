# wofi

> 一款用于基于 wlroots 的 Wayland 合成器的应用启动器，类似于 `rofi` 和 `dmenu`。
> 更多信息：<https://hg.sr.ht/~scoopta/wofi>。

- 显示应用列表：

`wofi --show drun`

- 显示所有命令的列表：

`wofi --show run`

- 将项目列表通过 `stdin` 传递并将选定的项目打印到 `stdout`：

`printf "{{Choice1\nChoice2\nChoice3}}" | wofi --dmenu`