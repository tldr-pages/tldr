# catimg

> 在终端中打印图像。
> 另请参见：`pixterm`，`chafa`。
> 更多信息：<https://github.com/posva/catimg>。

- 将 JPEG、PNG 或 GIF 打印到终端：

`catimg {{path/to/file}}`

- 将图像的 [r]esolution 加倍：

`catimg -r 2 {{path/to/file}}`

- 禁用 24 位颜色以获得更好的 [t]erminal 支持：

`catimg -t {{path/to/file}}`

- 指定自定义 [w]idth 或 [H]eight：

`catimg {{-w|-H}} {{40}} {{path/to/file}}`