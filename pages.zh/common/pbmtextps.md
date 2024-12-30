# pbmtextps

> 使用 PostScript 将文本渲染为 PBM 图像。
> 另见：`pbmtext`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pbmtextps.html>。

- 将单行文本渲染为 PBM 图像：

`pbmtextps "{{Hello World!}}" > {{path/to/output.pbm}}`

- 指定字体和字体大小：

`pbmtextps -font {{Times-Roman}} -fontsize {{30}} "{{Hello World!}}" > {{path/to/output.pbm}}`

- 指定所需的左边距和上边距：

`pbmtextps -leftmargin {{70}} -topmargin {{162}} "{{Hello World!}}" > {{path/to/output.pbm}}`

- 不将渲染的文本输出为 PBM 图像，而是输出一个 PostScript 程序，该程序将创建此图像：

`pbmtextps -dump-ps "{{Hello World!}}" > {{path/to/output.ps}}`