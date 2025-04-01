# rofi

> 应用程序启动器和窗口切换器。
> 更多信息：<https://github.com/davatorium/rofi>.

- 显示应用程序列表：

`rofi -show drun`

- 显示所有命令的列表：

`rofi -show run`

- 在窗口之间切换：

`rofi -show window`

- 将项目列表通过 `stdin` 管道传递，并将选中的项目打印到 `stdout`：

`printf "{{Choice1\nChoice2\nChoice3}}" | rofi -dmenu`