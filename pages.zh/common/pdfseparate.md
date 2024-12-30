# pdfseparate

> 可移植文档格式（PDF）文件页面提取器。
> 更多信息：<https://manpages.debian.org/latest/poppler-utils/pdfseparate.1.zh.html>。

- 从PDF文件中提取页面，并为每个页面生成一个单独的PDF文件：

`pdfseparate {{path/to/source_filename.pdf}} {{path/to/destination_filename-%d.pdf}}`

- 指定提取的起始页面：

`pdfseparate -f {{3}} {{path/to/source_filename.pdf}} {{path/to/destination_filename-%d.pdf}}`

- 指定提取的最后页面：

`pdfseparate -l {{10}} {{path/to/source_filename.pdf}} {{path/to/destination_filename-%d.pdf}}`