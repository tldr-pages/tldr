# pdftotext

> 将 PDF 文件转换为纯文本格式。
> 更多信息：<https://www.xpdfreader.com/pdftotext-man.html>.

- 将 `filename.pdf` 转换为纯文本并打印到 `stdout`：

`pdftotext {{filename.pdf}} -`

- 将 `filename.pdf` 转换为纯文本并保存为 `filename.txt`：

`pdftotext {{filename.pdf}}`

- 将 `filename.pdf` 转换为纯文本并保留布局：

`pdftotext -layout {{filename.pdf}}`

- 将 `input.pdf` 转换为纯文本并保存为 `output.txt`：

`pdftotext {{input.pdf}} {{output.txt}}`

- 将 `input.pdf` 的第 2、3 和 4 页转换为纯文本并保存为 `output.txt`：

`pdftotext -f {{2}} -l {{4}} {{input.pdf}} {{output.txt}}`
