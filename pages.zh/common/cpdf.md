# cpdf

> 操纵 PDF 文件。
> 更多信息：<https://www.coherentpdf.com/cpdfmanual/cpdfmanual.html>.

- 从源文档中选择第 1、2、3 和 6 页，并将这些页面写入目标文档：

`cpdf {{path/to/source_document.pdf}} {{1-3,6}} -o {{path/to/destination_document.pdf}}`

- 将两个文档合并为一个新文档：

`cpdf -merge {{path/to/source_document_one.pdf}} {{path/to/source_document_two.pdf}} -o {{path/to/destination_document.pdf}}`

- 显示文档的书签：

`cpdf -list-bookmarks {{path/to/document.pdf}}`

- 将文档拆分为十页的分块，将它们写入 `chunk001.pdf`、`chunk002.pdf` 等：

`cpdf -split {{path/to/document.pdf}} -o {{path/to/chunk%%%.pdf}} -chunk {{10}}`

- 使用 128 位加密加密文档，提供 `fred` 作为所有者密码和 `joe` 作为用户密码：

`cpdf -encrypt {{128bit}} {{fred}} {{joe}} {{path/to/source_document.pdf}} -o {{path/to/encrypted_document.pdf}}`

- 使用所有者密码 `fred` 解密文档：

`cpdf -decrypt {{path/to/encrypted_document.pdf}} owner={{fred}} -o {{path/to/decrypted_document.pdf}}`

- 显示文档的注释：

`cpdf -list-annotations {{path/to/document.pdf}}`

- 从现有文档创建一个新文档，并添加额外的元数据：

`cpdf -set-metadata {{path/to/metadata.xml}} {{path/to/source_document.pdf}} -o {{path/to/destination_document.pdf}}`