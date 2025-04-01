# pdfseparate

> 便携文档格式（PDF）文件页提取工具。
> 更多信息：<https://manpages.debian.org/latest/poppler-utils/pdfseparate.1.en.html>。

- 从 PDF 文件中提取每一页，并为每一页生成一个单独的 PDF 文件：

`pdfseparate {{path/to/source_filename.pdf}} {{path/to/destination_filename-%d.pdf}}`

- 指定提取的起始页：

`pdfseparate -f {{3}} {{path/to/source_filename.pdf}} {{path/to/destination_filename-%d.pdf}}`

- 指定提取的结束页：

`pdfseparate -l {{10}} {{path/to/source_filename.pdf}} {{path/to/destination_filename-%d.pdf}}`