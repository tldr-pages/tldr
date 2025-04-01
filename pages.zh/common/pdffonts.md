# pdffonts

> 便携式文档格式 (PDF) 文件字体信息查看器。
> 更多信息：<https://www.xpdfreader.com/pdffonts-man.html>。

- 打印 PDF 文件的字体信息：

`pdffonts {{path/to/file.pdf}}`

- 指定用户密码以绕过 PDF 文件的安全限制：

`pdffonts -upw {{password}} {{path/to/file.pdf}}`

- 指定所有者密码以绕过 PDF 文件的安全限制：

`pdffonts -opw {{password}} {{path/to/file.pdf}}`

- 打印关于在 PDF 文件光栅化时将使用的字体位置的附加信息：

`pdffonts -loc {{path/to/file.pdf}}`

- 打印关于在 PDF 文件转换为 PostScript 时将使用的字体位置的附加信息：

`pdffonts -locPS {{path/to/file.pdf}}`