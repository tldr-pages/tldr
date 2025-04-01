# pstoedit

> 将 PDF 文件转换为各种图像格式。
> 更多信息：<http://www.pstoedit.net>。

- 将 PDF 页面转换为 PNG 或 JPEG 格式：

`pstoedit -page {{page_number}} -f magick {{path/to/file.pdf}} {{page.png|page.jpg}}`

- 将多个 PDF 页面转换为编号图像：

`pstoedit -f magick {{path/to/file}} {{page%d.png|page%d.jpg}}`