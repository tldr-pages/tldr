# pic

> 用于 groff（GNU Troff）文档排版系统的图片预处理器。
> 另见 `groff` 和 `troff`。
> 更多信息请访问：<https://manned.org/pic>。

- 处理带有图片的输入，将输出保存以便将来与 groff 一起排版为 PostScript：

`pic {{path/to/input.pic}} > {{path/to/output.roff}}`

- 使用 [me] 宏包将带有图片的输入排版为 PDF：

`pic -T {{pdf}} {{path/to/input.pic}} | groff -{{me}} -T {{pdf}} > {{path/to/output.pdf}}`