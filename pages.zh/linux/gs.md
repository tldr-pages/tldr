# gs

> GhostScript 是一个 PDF 和 PostScript 解释器。
> 更多信息：<https://manned.org/gs>.

- 查看文件：

`gs -dQUIET -dBATCH {{file.pdf}}`

- 将 PDF 文件压缩为 150 dpi 的图像，适用于电子书设备阅读：

`gs -dNOPAUSE -dQUIET -dBATCH -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook -sOutputFile={{output.pdf}} {{input.pdf}}`

- 将 PDF 文件（第 1 到第 3 页）转换为分辨率为 150 dpi 的图像：

`gs -dQUIET -dBATCH -dNOPAUSE -sDEVICE=jpeg -r150 -dFirstPage={{1}} -dLastPage={{3}} -sOutputFile={{output_%d.jpg}} {{input.pdf}}`

- 从 PDF 文件中提取页面：

`gs -dQUIET -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile={{output.pdf}} {{input.pdf}}`

- 合并 PDF 文件：

`gs -dQUIET -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile={{output.pdf}} {{input1.pdf}} {{input2.pdf}}`

- 将 PostScript 文件转换为 PDF 文件：

`gs -dQUIET -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile={{output.pdf}} {{input.ps}}`