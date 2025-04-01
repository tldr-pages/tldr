# wl-paste

> 在 Wayland 剪贴板中粘贴内容。
> 参见: `wl-copy`, `xclip`。
> 更多信息: <https://github.com/bugaevc/wl-clipboard>。

- 粘贴剪贴板的内容：

`wl-paste`

- 粘贴主剪贴板的内容（高亮的文本）：

`wl-paste --primary`

- 将剪贴板的内容写入文件：

`wl-paste > {{path/to/file}}`

- 将剪贴板的内容通过管道传递给命令：

`wl-paste | {{command}}`
