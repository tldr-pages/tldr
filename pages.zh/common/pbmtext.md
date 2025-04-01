# pbmtext

> 将文本渲染为 PBM 图像。
> 参见：`pbmtextps`。
> 更多信息：<https://netpbm.sourceforge.net/doc/pbmtext.html>。

- 将单行文本渲染为 PBM 图像：

`pbmtext "{{Hello World!}}" > {{path/to/output.pbm}}`

- 将多行文本渲染为 PBM 图像：

`echo "{{Hello\nWorld!}}" | pbmtext > {{path/to/output.pbm}}`

- 使用提供的 PBM 文件作为自定义字体渲染文本：

`pbmtext -font {{path/to/font.pbm}} "{{Hello World!}}" > {{path/to/output.pbm}}`

- 指定字符和行之间的像素间距：

`echo "{{Hello\nWorld!}}" | pbmtext -space {{3}} -lspace {{10}} > {{path/to/output.pbm}}`
