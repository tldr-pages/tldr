# xpdf

> 便携文档格式（PDF）文件查看器。
> 更多信息：<https://www.xpdfreader.com/xpdf-man.html>。

- 打开一个 PDF 文件：

`xpdf {{path/to/file.pdf}}`

- 打开 PDF 文件中的特定页面：

`xpdf {{path/to/file.pdf}} :{{page_number}}`

- 打开一个压缩的 PDF 文件：

`xpdf {{path/to/file.pdf.tar}}`

- 全屏模式下打开 PDF 文件：

`xpdf -fullscreen {{path/to/file.pdf}}`

- 指定初始缩放级别：

`xpdf -z {{75}}% {{path/to/file.pdf}}`

- 指定初始缩放为页面宽度或全页面：

`xpdf -z {{page|width}} {{path/to/file.pdf}}`