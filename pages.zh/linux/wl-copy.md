# wl-copy

> 清空并复制到 Wayland 剪贴板。
> 另请参阅：`wl-paste`, `xclip`。
> 更多信息：<https://github.com/bugaevc/wl-clipboard>。

- 将文本复制到剪贴板：

`wl-copy "{{text}}"`

- 将命令（如 `ls`）的输出通过管道传递到剪贴板：

`{{ls}} | wl-copy`

- 只粘贴一次后清空剪贴板：

`wl-copy --paste-once "{{text}}"`

- 复制图像：

`wl-copy < {{path/to/image}}`

- 清空剪贴板：

`wl-copy --clear`