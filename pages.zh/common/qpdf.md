# qpdf

> 多功能 PDF 转换软件。
> 更多信息：<https://github.com/qpdf/qpdf>.

- 从 PDF 文件中提取第 1-3 页、第 5 页和第 6-10 页，并将它们另存为一个新的 PDF 文件：

`qpdf --empty --pages {{路径/到/input.pdf}} {{1-3,5,6-10}} -- {{路径/到/output.pdf}}`

- 合并（连接）多个 PDF 文件的所有页面，并将结果保存为一个新的 PDF 文件：

`qpdf --empty --pages {{路径/到/file1.pdf file2.pdf ...}} -- {{路径/到/output.pdf}}`

- 合并（连接）来自多个 PDF 文件的指定页面，并将结果保存为一个新的 PDF 文件：

`qpdf --empty --pages {{路径/到/file1.pdf}} {{1,6-8}} {{路径/到/file2.pdf}} {{3,4,5}} -- {{路径/到/output.pdf}}`

- 将每组 `n` 页写入一个单独的输出文件，并使用给定的文件名模式：

`qpdf --split-pages={{n}} {{路径/到/input.pdf}} {{路径/到/out_%d.pdf}}`

- 将 PDF 的某些页面旋转指定角度：

`qpdf --rotate={{90:2,4,6}} --rotate={{180:7-8}} {{路径/到/input.pdf}} {{路径/到/output.pdf}}`

- 从受密码保护的文件中移除密码：

`qpdf --password={{password}} --decrypt {{路径/到/input.pdf}} {{路径/到/output.pdf}}`
