# qpdf

> 多功能 PDF 转换软件。
> 更多信息：<https://github.com/qpdf/qpdf>。

- 从 PDF 文件中提取第 1-3 页，第 5 页和第 6-10 页，并将其保存为另一个文件：

`qpdf --empty --pages {{path/to/input.pdf}} {{1-3,5,6-10}} -- {{path/to/output.pdf}}`

- 合并（连接）多个 PDF 文件的所有页面，并将结果保存为一个新的 PDF：

`qpdf --empty --pages {{path/to/file1.pdf file2.pdf ...}} -- {{path/to/output.pdf}}`

- 从一组 PDF 文件中合并（连接）给定的页面，并将结果保存为一个新的 PDF：

`qpdf --empty --pages {{path/to/file1.pdf}} {{1,6-8}} {{path/to/file2.pdf}} {{3,4,5}} -- {{path/to/output.pdf}}`

- 将每组 `n` 页写入一个单独的输出文件，文件名遵循给定的模式：

`qpdf --split-pages={{n}} {{path/to/input.pdf}} {{path/to/out_%d.pdf}}`

- 以给定角度旋转 PDF 的某些页面：

`qpdf --rotate={{90:2,4,6}} --rotate={{180:7-8}} {{path/to/input.pdf}} {{path/to/output.pdf}}`

- 从受密码保护的文件中移除密码：

`qpdf --password={{password}} --decrypt {{path/to/input.pdf}} {{path/to/output.pdf}}`