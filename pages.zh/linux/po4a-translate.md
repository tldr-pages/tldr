# po4a-translate

> 将 PO 文件转换回文档格式。
> 提供的 PO 文件应该是由 `po4a-gettextize` 生成的 POT 文件的翻译版本。
> 更多信息：<https://po4a.org/man/man1/po4a-translate.1.php>。

- 将翻译后的 PO 文件转换回文档：

`po4a-translate --format {{text}} --master {{path/to/master.doc}} --po {{path/to/result.po}} --localized {{path/to/translated.txt}}`

- 列出所有可用的格式：

`po4a-translate --help-format`
