# pdffonts

> 可移植文档格式（PDF）文件字体信息查看器。
> 更多信息：<https://www.xpdfreader.com/pdffonts-man.html>。

- 打印 PDF 文件字体信息：

`pdffonts {{path/to/file.pdf}}`

- 指定 PDF 文件的用户密码以绕过安全限制：

`pdffonts -upw {{password}} {{path/to/file.pdf}}`

- 指定 PDF 文件的所有者密码以绕过安全限制：

`pdffonts -opw {{password}} {{path/to/file.pdf}}`

- 打印 PDF 文件在栅格化时将使用的字体位置的附加信息：

`pdffonts -loc {{path/to/file.pdf}}`

- 打印 PDF 文件在转换为 PostScript 时将使用的字体位置的附加信息：

`pdffonts -locPS {{path/to/file.pdf}}`