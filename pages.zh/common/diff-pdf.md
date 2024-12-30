# diff-pdf

> 比较两个PDF文件。
> 更多信息：<https://github.com/vslavik/diff-pdf>。

- 比较PDF文件，使用返回代码指示更改（`0` = 没有差异，`1` = PDF文件不同）：

`diff-pdf {{path/to/a.pdf}} {{path/to/b.pdf}}`

- 比较PDF文件，输出一个视觉上突出差异的PDF：

`diff-pdf --output-diff={{path/to/diff.pdf}} {{path/to/a.pdf}} {{path/to/b.pdf}}`

- 比较PDF文件，在简单的GUI中查看差异：

`diff-pdf --view {{path/to/a.pdf}} {{path/to/b.pdf}}`