# catimg

> 在终端中打印图像。
> 参见: `pixterm`, `chafa`。
> 更多信息: <https://manned.org/catimg>。

- 将 JPEG、PNG 或 GIF 图像打印到终端：

`catimg {{path/to/file}}`

- 将图像的分辨率提高一倍：

`catimg -r 2 {{path/to/file}}`

- 禁用 24 位颜色以获得更好的终端支持：

`catimg -t {{path/to/file}}`

- 指定自定义宽度或高度：

`catimg {{-w|-H}} {{40}} {{path/to/file}}`
