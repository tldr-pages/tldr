# pic

> 用于 groff (GNU Troff) 文档格式系统的图片预处理器。
> 请参阅 `groff` 和 `troff`。
> 更多信息：<https://manned.org/pic>。

- 处理带有图片的输入，并保存输出以供后续使用 groff 转换为 PostScript：

`pic {{path/to/input.pic}} > {{path/to/output.roff}}`

- 使用 [me] 宏包将带有图片的输入排版成 PDF：

`pic -T {{pdf}} {{path/to/input.pic}} | groff -{{me}} -T {{pdf}} > {{path/to/output.pdf}}`