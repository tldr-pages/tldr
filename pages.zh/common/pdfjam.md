# pdfjam

> 用于合并 PDF 文件的 LaTeX pdfpages 包的 Shell 前端。
> 更多信息：<https://github.com/rrthomas/pdfjam>。

- 合并两个（或多个）PDF 文件：

`pdfjam {{path/to/file1.pdf}} {{path/to/file2.pdf}} --outfile {{path/to/output_file.pdf}}`

- 合并每个文件的第一页：

`pdfjam {{files...}} 1 --outfile {{path/to/output_file.pdf}}`

- 合并两个 PDF 文件的子范围：

`pdfjam {{path/to/file1.pdf 3-5,1}} {{path/to/file2.pdf 4-6}} --outfile {{path/to/output_file.pdf}}`

- 通过叠加签名对 A4 页面进行签名（对于其他格式，调整 delta 以适应高度）：

`pdfjam {{path/to/file.pdf}} {{path/to/signature}} --fitpaper true --outfile {{path/to/signed.pdf}} --nup "{{1x2}}" --delta "{{0 -842pt}}"`

- 将输入文件的页面排列成一个华丽的 2x2 网格：

`pdfjam {{path/to/file.pdf}} --nup {{2x2}} --suffix {{4up}} --preamble '{{\usepackage{fancyhdr} \pagestyle{fancy}}}'`

- 反转每个给定文件中的页面顺序并连接它们：

`pdfjam {{files...}} {{last-1}} --suffix {{reversed}}`