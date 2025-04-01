# pdfinfo

> 便携式文档格式（PDF）文件信息查看器。
> 更多信息：<https://www.xpdfreader.com/pdfinfo-man.html>.

- 打印 PDF 文件信息：

`pdfinfo {{path/to/file.pdf}}`

- 指定 PDF 文件的用户密码以绕过安全限制：

`pdfinfo -upw {{password}} {{path/to/file.pdf}}`

- 指定 PDF 文件的所有者密码以绕过安全限制：

`pdfinfo -opw {{password}} {{path/to/file.pdf}}`