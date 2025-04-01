# diff-pdf

> 比较两个 PDF 文件。
> 更多信息：<https://github.com/vslavik/diff-pdf>。

- 比较 PDF 文件，使用返回代码指示差异（`0` = 无差异，`1` = PDF 文件不同）：

`diff-pdf {{path/to/a.pdf}} {{path/to/b.pdf}}`

- 比较 PDF 文件，输出一个带有视觉高亮差异的 PDF：

`diff-pdf --output-diff={{path/to/diff.pdf}} {{path/to/a.pdf}} {{path/to/b.pdf}}`

- 比较 PDF 文件，在简单的 GUI 中查看差异：

`diff-pdf --view {{path/to/a.pdf}} {{path/to/b.pdf}}`