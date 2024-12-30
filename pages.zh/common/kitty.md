# kitty

> 一个快速、功能丰富的基于 GPU 的终端模拟器。
> 更多信息：<https://sw.kovidgoyal.net/kitty/>.

- 打开一个新的终端：

`kitty`

- 打开一个指定标题的终端窗口：

`kitty --title "{{title}}"`

- 启动主题选择内置程序：

`kitty +kitten themes`

- 在终端中显示图像：

`kitty +kitten icat {{path/to/image}}`

- 将 `stdin` 的内容复制到剪贴板：

`echo {{example}} | kitty +kitten clipboard`