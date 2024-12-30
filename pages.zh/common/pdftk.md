# pdftk

> PDF 工具包。
> 更多信息：<https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit>。

- 从 PDF 文件中提取第 1-3 页、第 5 页和第 6-10 页，并将其保存为另一个文件：

`pdftk {{input.pdf}} cat {{1-3 5 6-10}} output {{output.pdf}}`

- 合并（连接）一系列 PDF 文件，并将结果保存为另一个文件：

`pdftk {{file1.pdf file2.pdf ...}} cat output {{output.pdf}}`

- 将 PDF 文件的每一页拆分为一个单独的文件，并使用给定的文件名输出模式：

`pdftk {{input.pdf}} burst output {{out_%d.pdf}}`

- 将所有页面顺时针旋转 180 度：

`pdftk {{input.pdf}} cat {{1-endsouth}} output {{output.pdf}}`

- 将第三页顺时针旋转 90 度，其他页面保持不变：

`pdftk {{input.pdf}} cat {{1-2 3east 4-end}} output {{output.pdf}}`