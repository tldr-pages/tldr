# po4a-translate

> 将 PO 文件转换回文档格式。
> 提供的 PO 文件应为通过 `po4a-gettextize` 生成的 POT 文件的翻译。
> 更多信息：<https://po4a.org/man/man1/po4a-translate.1.php>。

- 将翻译后的 PO 文件转换回文档：

`po4a-translate --format {{文本}} --master {{路径/到/主文档.doc}} --po {{路径/到/结果.po}} --localized {{路径/到/翻译过的.txt}}`

- 列出所有可用格式：

`po4a-translate --help-format`