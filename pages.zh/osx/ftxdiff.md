# ftxdiff

> 比较两个字体之间的差异。
> 更多信息：<https://developer.apple.com/fonts>.

- 将差异输出到特定的文本文件中：

`ftxdiff --output {{path/to/fontdiff_file.txt}} {{path/to/font_file1.ttc}} {{path/to/font_file2.ttc}}`

- 在输出中包含字形名称：

`ftxdiff --include-glyph-names`

- 在输出中包含 Unicode 名称：

`ftxdiff --include-unicode-names`