# po4a-updatepo

> 更新文档的翻译（以 PO 格式）。
> 更多信息：<https://po4a.org/man/man1/po4a-updatepo.1.php>.

- 根据其源文件的修改更新 PO 文件：

`po4a-updatepo --format {{text}} --master {{path/to/master.txt}} --po {{path/to/result.po}}`

- 列出可用的格式：

`po4a-updatepo --help-format`

- 根据其源文件的修改更新多个 PO 文件：

`po4a-updatepo --format {{text}} --master {{path/to/master.txt}} --po {{path/to/po1.po}} --po {{path/to/po2.po}}`
