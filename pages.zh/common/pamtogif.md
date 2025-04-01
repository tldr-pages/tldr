# pamtogif

> 将 Netpbm 图像转换为非动画 GIF 图像。
> 参见：`giftopnm`, `gifsicle`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pamtogif.html>。

- 将 Netpbm 图像转换为非动画 GIF 图像：

`pamtogif {{path/to/image.pam}} > {{path/to/output.gif}}`

- 在输出的 GIF 文件中指定颜色为透明：

`pamtogif -transparent {{color}} {{path/to/image.pam}} > {{path/to/output.gif}}`

- 在输出的 GIF 文件中包含指定的文本作为注释：

`pamtogif -comment "{{Hello World!}}" {{path/to/image.pam}} > {{path/to/output.gif}}`
