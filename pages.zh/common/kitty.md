# kitty

> 一个快速、功能丰富、基于 GPU 的终端模拟器。
> 更多信息：<https://sw.kovidgoyal.net/kitty/>.

- 打开一个新的终端：

`kitty`

- 使用指定的窗口标题打开一个终端：

`kitty --title "{{title}}"`

- 启动内置的主题选择器：

`kitty +kitten themes`

- 在终端中显示图片：

`kitty +kitten icat {{path/to/image}}`

- 将 `stdin` 的内容复制到剪贴板：

`echo {{example}} | kitty +kitten clipboard`