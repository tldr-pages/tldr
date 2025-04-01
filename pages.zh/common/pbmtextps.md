# pbmtextps

> 使用 PostScript 将文本渲染为 PBM 图像。
> 参见：`pbmtext`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pbmtextps.html>。

- 将一行文本渲染为 PBM 图像：

`pbmtextps "{{Hello World!}}" > {{path/to/output.pbm}}`

- 指定字体和字体大小：

`pbmtextps -font {{Times-Roman}} -fontsize {{30}} "{{Hello World!}}" > {{path/to/output.pbm}}`

- 指定所需的左边界和顶边界：

`pbmtextps -leftmargin {{70}} -topmargin {{162}} "{{Hello World!}}" > {{path/to/output.pbm}}`

- 不输出渲染的文本作为 PBM 图像，而是输出一个可以生成此图像的 PostScript 程序：

`pbmtextps -dump-ps "{{Hello World!}}" > {{path/to/output.ps}}`