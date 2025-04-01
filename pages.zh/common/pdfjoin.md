# pdfjoin

> 基于 pdfjam 的 PDF 合并工具。
> 更多信息：<https://github.com/rrthomas/pdfjam-extras>.

- 将两个 PDF 文件合并成一个，默认后缀为 "joined"：

`pdfjoin {{path/to/file1.pdf}} {{path/to/file2.pdf}}`

- 将每个给定文件的第一页合并在一起：

`pdfjoin {{path/to/file1.pdf path/to/file2.pdf ...}} {{1}} --outfile {{output_file}}`

- 将第 3 到 5 页和第 1 页保存到一个新的 PDF 文件中，自定义后缀：

`pdfjoin {{path/to/file.pdf}} {{3-5,1}} --suffix {{rearranged}}`

- 合并两个 PDF 文件的页面子范围：

`pdfjoin {{/path/to/file1.pdf}} {{2-}} {{file2}} {{last-3}} --outfile {{output_file}}`