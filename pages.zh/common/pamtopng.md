# pamtopng

> 将 PAM 图像转换为 PNG。
> 参见：`pnmtopng`，`pngtopam`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pamtopng.html>。

- 将指定的 PAM 图像转换为 PNG：

`pamtopng {{path/to/image.pam}} > {{path/to/output.png}}`

- 在输出图像中将指定颜色标记为透明：

`pamtopng -transparent {{color}} {{path/to/image.pam}} > {{path/to/output.png}}`

- 将指定文件中的文本作为 tEXt 块包含在输出中：

`pamtopng -text {{path/to/file.txt}} {{path/to/image.pam}} > {{path/to/output.png}}`

- 使输出文件以 Adam7 格式交错：

`pamtopng -interlace {{path/to/image.pam}} > {{path/to/output.png}}`