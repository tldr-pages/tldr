# po4a-gettextize

> 将文件转换为 PO 文件。
> 更多信息：<https://po4a.org/man/man1/po4a-gettextize.1.php>。

- 将文本文件转换为 PO 文件：

`po4a-gettextize --format {{text}} --master {{path/to/master.txt}} --po {{path/to/result.po}}`

- 列出所有可用的格式：

`po4a-gettextize --help-format`

- 将文本文件及其翻译文档转换为 PO 文件（`-l` 选项可以多次提供）：

`po4a-gettextize --format {{text}} --master {{path/to/master.txt}} --localized {{path/to/translated.txt}} --po {{path/to/result.po}}`
