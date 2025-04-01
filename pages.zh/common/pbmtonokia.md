# pbmtonokia

> 将 PBM 图像转换为诺基亚的智能消息格式之一。
> 更多信息：<https://netpbm.sourceforge.net/doc/pbmtonokia.html>.

- 将 PBM 图像转换为诺基亚运营商标志的十六进制代码：

`pbmtonokia -fmt NEX_NOL -net {{network_operator_code}} {{path/to/image.pbm}} > {{path/to/output.hex}}`

- 将 PBM 图像转换为诺基亚群组图形的十六进制代码：

`pbmtonokia -fmt NEX_NGG {{path/to/image.pbm}} > {{path/to/output.hex}}`

- 将 PBM 图像转换为包含指定文本的诺基亚图片消息的十六进制代码：

`pbmtonokia -fmt NEX_NPM -txt {{text_message}} {{path/to/image.pbm}} > {{path/to/output.hex}}`

- 将 PBM 图像转换为诺基亚运营商标志文件：

`pbmtonokia -fmt NOL {{path/to/image.pbm}} > {{path/to/output.nol}}`

- 将 PBM 图像转换为诺基亚群组图形文件：

`pbmtonokia -fmt NGG {{path/to/image.pbm}} > {{path/to/output.ngg}}`

- 将 PBM 图像转换为诺基亚图片消息文件：

`pbmtonokia -fmt NPM {{path/to/image.pbm}} > {{path/to/output.npm}}`