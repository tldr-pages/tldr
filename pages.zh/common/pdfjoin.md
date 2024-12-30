# pdfjoin

> 基于 pdfjam 的 PDF 合并工具。
> 更多信息：<https://github.com/rrthomas/pdfjam-extras>。

- 将两个 PDF 合并为一个，默认后缀为 "joined"：

`pdfjoin {{path/to/file1.pdf}} {{path/to/file2.pdf}}`

- 合并每个给定文件的第一页：

`pdfjoin {{path/to/file1.pdf path/to/file2.pdf ...}} {{1}} --outfile {{output_file}}`

- 将第3到第5页以及第1页保存到一个新的 PDF，并使用自定义后缀：

`pdfjoin {{path/to/file.pdf}} {{3-5,1}} --suffix {{rearranged}}`

- 从两个 PDF 中合并页面子范围：

`pdfjoin {{/path/to/file1.pdf}} {{2-}} {{file2}} {{last-3}} --outfile {{output_file}}`