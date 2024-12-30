# wl-copy

> 清除并复制到 Wayland 剪贴板。
> 另见：`wl-paste`，`xclip`。
> 更多信息：<https://github.com/bugaevc/wl-clipboard>。

- 将文本复制到剪贴板：

`wl-copy "{{text}}"`

- 将命令（`ls`）的输出通过管道传送到剪贴板：

`{{ls}} | wl-copy`

- 仅复制一次，然后清除：

`wl-copy --paste-once "{{text}}"`

- 复制图像：

`wl-copy < {{path/to/image}}`

- 清除剪贴板：

`wl-copy --clear`